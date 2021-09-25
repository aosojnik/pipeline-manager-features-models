import pandas as pd
import numpy as np

from scipy.signal import find_peaks, butter, lfilter_zi, lfilter
from dataclasses import dataclass

pd.set_option('mode.chained_assignment', None)

from datetime import datetime

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
DATETIME_DB_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

def ensure_datetime(date):
    """Ensures that the date is in the datetime format. Needed due to the different accessors,HTTP accessor converts everything to strings, while native Python Mongo driver already provides datetime objects."""
    t = type(date)
    if t == datetime:
        return date
    elif t == dict:
        return datetime.strptime(date['$date'], DATETIME_DB_FORMAT)
    else:
        return datetime.strptime(date, DATETIME_FORMAT)


def filter_array(arej:"np.ndarray to be filtered"):
    """LP filter for 1d array, returns filtered array"""
    b, a = butter(1, .2)
    zi = lfilter_zi(b,a)
    z, _ = lfilter(b,a,arej,zi=zi*arej[0])
    return z


def peak_finder(df: "pandas dataframe with Unixtime and Magnitude columns",
               LPfilter: "bool,Whether or not to LPF the Magnitude column" = False,
               sigma: "scalar number, How many std above mean should peaks be to count" = 5):
    """Finds peaks and valleys in df.Magnitude. 
    LPFilters Magnitudes and then finds peaks.
    Returns peak indices and magnitudes."""
    assert "Magnitude" in df.columns
    assert "Unixtime" in df.columns
    
    mean = df.Magnitude.mean()
    x = df.Magnitude.values - mean
    if LPfilter:
        x = filter_array(x)
    peak_indices, peak_dic = find_peaks(x, threshold=sigma*np.std(x))
    valley_indices, valley_dic = find_peaks(-x, threshold=sigma*np.std(x))
    
    peak_indices = [*peak_indices, *valley_indices, *peak_indices,*valley_indices]
    peak_heights = [*peak_dic["left_thresholds"], *valley_dic["left_thresholds"], *peak_dic["right_thresholds"], *valley_dic["right_thresholds"]]
    zipano = [(index ,height) for index, height in zip(peak_indices,peak_heights)]
    sort_zipano = sorted(zipano, key=lambda item: item[0])
    peak_indices, peak_heights = [i[0] for i in sort_zipano], [i[1] for i in sort_zipano]
    return peak_indices, peak_heights

def group_peaks(df: "Pandas dataframe with Unixtime and Magnitude columns",
                omega: "group window in seconds" = 10,
                LPfilter: "bool,Whether or not to LPF the Magnitude column"=False,
                sigma: "scalar number, How many std above mean should peaks be to count"=5):
    """Groups peaks in df.Magnitude with window omega. Returns a list of dataclass instances:
        @dataclass
        class PeakGroup:
            start_unixtime : int
            heights : list
            maxheight : float
            sumheight : float
    """
    peak_indices, peak_heights = peak_finder(df, LPfilter=LPfilter, sigma=sigma)
    
    x = df.Magnitude.copy().values
    t = df.Unixtime.copy().values
    

    @dataclass
    class PeakGroup:
        start_unixtime : int
        heights : list
        maxheight : float

    peak_groups = []

    for i, peak_index in enumerate(sorted(peak_indices)):
        current_peak_time = t[peak_index]
        if peak_groups:
            last_peak_time = peak_groups[-1].start_unixtime
        else:
            last_peak_time = 0

        #test if time is within omega from the last peak:
        if current_peak_time > last_peak_time + omega: #omega is in seconds, time is in s as well
            #create new peak group
            peak_groups.append(
                PeakGroup(t[peak_index], [x[peak_index]], x[peak_index])
                                )
        else:
            #extend the previous peak group
            peak_groups[-1].heights.append(x[peak_index])
            peak_groups[-1].maxheight = max(x[peak_index], peak_groups[-1].maxheight)
    return peak_groups

def discriminate_strong_weak(df: "Pandas dataframe with Unixtime and Magnitude columns",
                    alpha: "float, parameter for discriminating non-transition peak groups" = 0.2,
                    omega: "float, group lenght in seconds" = 30,
                    omegastar: "float, window in minutes for group counting" = 10,
                    LPfilter: "bool, Whether or not to LPF the Magnitude column" = False,
                    sigma: "float, How many std above mean should peaks be to count" = 5.5):
    """Performs peak finding, grouping and discrimination. Returns [strong peak times], [weak peak times]"""
    df = df.reset_index(drop=True)
    peak_groups = group_peaks(df, omega=omega, LPfilter=LPfilter, sigma=sigma)
    
    measurement_start_time = df.Unixtime.min()
    measurement_end_time = df.Unixtime.max()
    
    if len(peak_groups) >= 2:
        peak_groups.sort(key=lambda g: g.maxheight, reverse=True) #sort peak heights so top 2 heights can be extracted
        strong_peak_level = 0.5*peak_groups[0].maxheight + 0.5*peak_groups[1].maxheight
        mean_peak_level = np.mean([g.maxheight for g in peak_groups])
        
        peak_groups.sort(key=lambda g: g.start_unixtime) #sort peaks according to the start time of their group
        #determine border between strong and weak peaks and extract their times
        border_level = alpha*(strong_peak_level - mean_peak_level) + mean_peak_level

        strong_peaks_times = [g.start_unixtime for g in peak_groups if g.maxheight >= border_level]
        weak_peaks_times = [g.start_unixtime for g in peak_groups if g.maxheight < border_level]
        
        return strong_peaks_times, weak_peaks_times
    else:
        return [g.start_unixtime for g in peak_groups], []


def section_peaks(strong_peak_times: "array of strong peak times",
                   weak_peak_times: "array of weak peak times",
                   measurement_start: "posix_s of start of measurement",
                   measurement_end: "posix_s of end of measurement"):
    """Returns dict={section_start_time:[weak peaks in section times],...}
    The first section will start at the beggining of the measurement, 
    so in total the number of sections will equal the number of strong peaks plus one."""
    sections = sorted([measurement_start, *strong_peak_times, measurement_end])
    dic = dict()
    for i, sec_start in enumerate(sections[:-1]):
        dic[sec_start] = [weak for weak in weak_peak_times if (weak >= sec_start)&(weak < sections[i+1])    ]
    return dic

    
def correct_strongs(strong_dict: "dictionary, result of section_peaks function"):
    """Corrects strong peaks that should be classified as weak. Returns corrected strong_dict."""
    def correct_for_inbed_strongs(strong_dict):
        """Tests whether we have consecutive sections with weak peaks, separated by 
        strong peaks which should be weak. Returns corrected strong_dict"""
        ordered_start_times = sorted(list(strong_dict.keys()))
        for i, time in enumerate(ordered_start_times):
            if i == len(ordered_start_times)-1:
                continue
            current_weaks     = strong_dict[time]
            next_weaks        = strong_dict[ordered_start_times[i+1]]

            if current_weaks != [] and next_weaks != []:
                strong_dict[time].append(ordered_start_times[i+1])
                del strong_dict[ordered_start_times[i+1]]
                return strong_dict
        return strong_dict
    
    def correct_for_empty_bed_strongs(strong_dict):
        """Test for consecutive sections without peaks, separated by 
        strong peaks."""
        ordered_start_times = sorted(list(strong_dict.keys()))
        for i, time in enumerate(ordered_start_times):
            pass
            if i == len(ordered_start_times)-1:
                continue
            if  i == len(ordered_start_times)-2:
                #Special treatment on account of not being able to look two sections into the future. Also, merging is different.
                next_time          = ordered_start_times[i+1]
                current_weaks      = strong_dict[time]
                next_weaks         = strong_dict[next_time]
                if current_weaks   == next_weaks == []:
                    #Strong peak that defines start of 'next' section will be added to 'current' section as a weak peak, but the section itself will remain
                    strong_dict[time].append(next_time)
            else:
                next_time          = ordered_start_times[i+1]
                next_next_time     = ordered_start_times[i+2]
                current_weaks      = strong_dict[time]
                next_weaks         = strong_dict[next_time]
                next_next_weaks    = strong_dict[next_next_time]
                if  current_weaks  == next_weaks == []:
                    dt1 = abs(time-next_time)
                    dt2 = abs(next_next_time - next_time)
                    if dt2 <= dt1:
                        next_weaks.extend(next_next_weaks)
                        next_weaks.append(next_next_time)
                        strong_dict[next_time].extend(next_weaks)
                        del strong_dict[next_next_time]
                        return strong_dict
                    else:
                        current_weaks.extend(next_weaks)
                        current_weaks.append(next_time)
                        strong_dict[time].extend(current_weaks)
                        del strong_dict[time]
                        return strong_dict
        return strong_dict
    for i in range(len(strong_dict)):
        """Since both helper functions only do one pass over the sections, multiple passes have to be made."""
        strong_dict = correct_for_empty_bed_strongs(strong_dict)
        strong_dict = correct_for_inbed_strongs(strong_dict) 
    return strong_dict


    
def test_strong_dict(strong_dict):
    """Debugging: Tests if all weak peaks are in the right section."""
    ordered_start_times = sorted(list(strong_dict.keys()))
    for i, current_time in enumerate(ordered_start_times[:-1]):
        next_time = ordered_start_times[i+1]
        current_weaks = strong_dict[current_time]
        for weak in current_weaks:
            if not (weak >= current_time)&(weak <= next_time):
                raise AttributeError(f"""Your strong dict is not sorted correctly and you should feel bad!
                Error at {current_time}, weak {weak}!
                Index of section: {i}""")


def calculate_strong_peaks(inputs):
    df = pd.DataFrame.from_records(inputs['feat_bed_accel_magnitude'], columns=['Unixtime', 'timestep', 'Magnitude'])
    df.drop(columns=['timestep'], inplace=True)

    strong_peak_times, weak_peak_times = discriminate_strong_weak(df=df, alpha=0.2, omega=30, omegastar=5, LPfilter=False, sigma=8)

    measurement_start_time, measurement_end_time = df.Unixtime.min(), df.Unixtime.max()

    
    strong_dic = section_peaks(strong_peak_times,
                               weak_peak_times,
                               measurement_start_time, 
                               measurement_end_time
                              )

    return strong_dic

def fuse_with_reliability(*pairs):
    s = sum(w * v for w, v in pairs if v) # weighted sum
    s_w = sum(w for w, v in pairs if v) # sum of weights
    return s / s_w if s_w else None