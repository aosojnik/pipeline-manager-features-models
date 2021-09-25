#!/usr/bin/python3

import numpy as np
import pandas as pd
import math

from scipy.stats import variation
from scipy.fftpack import fft, ifft, rfft
from scipy.interpolate import interp1d
from scipy.special import entr

def interpolate(data, wanted_freq, timestep):
    x_old = np.linspace(0, len(data)-1, num=len(data), retstep=True)[0]
    x_new = np.linspace(0, len(data)-1, num=timestep*wanted_freq, retstep=True)[0]
    f2_x = interp1d(x_old, data, kind='linear')
    return f2_x(x_new)


def interpolate3D(data, wanted_freq, timestep):
    x_old = np.linspace(0, len(data)-1, num=len(data), retstep=True)[0]
    x_new = np.linspace(0, len(data)-1, num=timestep * wanted_freq, retstep=True)[0]
    df = pd.DataFrame(data)

    f2_x = interp1d(x_old, df['x'], kind='linear')
    f2_y = interp1d(x_old, df['y'], kind='linear')
    f2_z = interp1d(x_old, df['z'], kind='linear')

    df_new = pd.DataFrame()
    df_new['x'] = f2_x(x_new)
    df_new['y'] = f2_y(x_new)
    df_new['z'] = f2_z(x_new)

    data_new = []
    for index, row in df_new.iterrows():
        data_new.append({'x': row.x, 'y': row.y, 'z': row.z})

    return data_new


# If α =0.5 then the RC time constant is equal to the sampling period. If  α << 0.5, then RC is significantly
# larger than the sampling interval
def low_pass_filter(r_list, alpha):
    num_sensors = int(len(r_list)/3)
    t_list = []
    for i in range(0, num_sensors):
        t_x = []
        t_y = []
        t_z = []
        t_x.insert(0, alpha*r_list[3*i][0])
        t_y.insert(0, alpha*r_list[3*i + 1][0])
        t_z.insert(0, alpha*r_list[3*i + 2][0])
        for j in range(1,  len(r_list[3*i])):
            t_x.insert(j, r_list[3*i][j - 1] + alpha * (r_list[3*i][j] - t_x[j - 1]))
            t_y.insert(j, r_list[3*i + 1][j - 1] + alpha * (r_list[3*i + 1][j] - t_y[j - 1]))
            t_z.insert(j, r_list[3*i + 2][j - 1] + alpha * (r_list[3*i + 2][j] - t_z[j - 1]))
        t_list.append(t_x)
        t_list.append(t_y)
        t_list.append(t_z)
    return t_list


# A small α implies that the output will decay quickly and will require large changes in the input (
# i.e., (x[i] - x[i-1]) is large) to cause the output to change much.
# A large α implies that the output will decay very slowly but will also be strongly influenced by
# even small changes in input.
def high_pass_filter(r_list, alpha):
    num_sensors = int(len(r_list)/3)
    t_list = []
    for i in range(0, num_sensors):
        t_x = []
        t_y = []
        t_z = []
        t_x.insert(0, alpha*r_list[3*i][0])
        t_y.insert(0, alpha*r_list[3*i + 1][0])
        t_z.insert(0, alpha*r_list[3*i + 2][0])
        for j in range(1,  len(r_list[3*i])):
            t_x.insert(j, alpha*(t_x[j - 1] + r_list[3*i][j] - r_list[3*i][j - 1]))
            t_y.insert(j, alpha*(t_y[j - 1] + r_list[3*i + 1][j] - r_list[3*i + 1][j - 1]))
            t_z.insert(j, alpha*(t_z[j - 1] + r_list[3*i + 2][j] - r_list[3*i + 2][j - 1]))
        t_list.append(t_x)
        t_list.append(t_y)
        t_list.append(t_z)
    return t_list


# [x, y, z]
def calculate_magnitudes(r_list):
    num_sensors = int(len(r_list) / 3)
    t_list = []
    for i in range(0, num_sensors):
        t_temp = []
        for j in range(0, len(r_list[3 * i])):
            t_temp.append(
                math.sqrt(pow(r_list[3 * i][j], 2) + pow(r_list[3 * i + 1][j], 2) + pow(r_list[3 * i + 2][j], 2)))
        t_list.append(t_temp)

    return t_list


def mean(r_list):
    t_list = []
    for r in r_list:
        t_list.append(np.mean(r))
    return t_list


# [x, y, z]
def total_mean(r_list):
    num_sensors = int(len(r_list) / 3)
    t_list = []
    for i in range(0, num_sensors):
        t_temp = []
        for j in range(0, len(r_list[3 * i])):
            t_temp.append(r_list[3 * i][j] + r_list[3 * i + 1][j] + r_list[3 * i + 2][j])
        t_list.append(np.mean(t_temp))
    return t_list


def area(r_list):
    t_list = []
    for r in r_list:
        t_list.append(sum(r))
    return t_list


# X-Y, X-Z, and Y-Z
def distance(r_list):
    num_sensors = int(len(r_list) / 3)
    t_list = []
    for i in range(0, num_sensors):
        # X-Y
        t_list.append(np.mean(r_list[3 * i]) - np.mean(r_list[3 * i + 1]))
        # X-Z
        t_list.append(np.mean(r_list[3 * i]) - np.mean(r_list[3 * i + 2]))
        # Y-Z
        t_list.append((np.mean(r_list[3 * i + 1]) - np.mean(r_list[3 * i + 2])))

    return t_list


# Mean of absolute signal value
def mean_absolute(r_list):
    t_list = []
    for r in r_list:
        t_list.append(np.mean(np.absolute(r)))
    return t_list


# Cumulative sum over absolute signal value - acceleration
# per sensor
# per signal
# output
# [sum(abs(x)), sum(abs(y)), sum(abs(z)), sum(abs(x)+abs(y)+abs(z))] per sensor
# [sum(abs(x)), sum(abs(y)), sum(abs(z)), sum(abs(x)+abs(y)+abs(z))] over all sensors
def sum_absolute_signal(r_list):
    # check if there are multiple sensors attached
    num_sensors = int(len(r_list) / 3)
    t_list = []
    s_list = [0] * 4

    # per sensor
    for i in range(0, num_sensors):
        # axis
        t_list.append(sum(np.absolute(r_list[3 * i])))
        t_list.append(sum(np.absolute(r_list[3 * i + 1])))
        t_list.append(sum(np.absolute(r_list[3 * i + 2])))

        s_list[0] = s_list[0] + sum(np.absolute(r_list[3 * i]))
        s_list[1] = s_list[1] + sum(np.absolute(r_list[3 * i + 1]))
        s_list[2] = s_list[2] + sum(np.absolute(r_list[3 * i + 2]))

        temp = []
        # all axis
        for j in range(0, len(r_list[3 * i])):
            temp.append(abs(r_list[3 * i][j]) + abs(r_list[3 * i + 1][j]) + abs(r_list[3 * i + 2][j]))

        t_list.append(sum(temp))
        s_list[3] = s_list[3] + sum(temp)

    return t_list, s_list


def calculate_fft(r_list):
    num_sensors = int(len(r_list) / 3)
    t_list = []
    m_list = []
    norm_list = []
    for i in range(0, num_sensors):
        fft_x = np.fft.fft(r_list[3 * i])
        fft_y = np.fft.fft(r_list[3 * i + 1])
        fft_z = np.fft.fft(r_list[3 * i + 2])

        t_list.append(abs(fft_x))
        t_list.append(abs(fft_y))
        t_list.append(abs(fft_z))

        m_x = calculate_fft_mag(abs(fft_x))
        m_y = calculate_fft_mag(abs(fft_y))
        m_z = calculate_fft_mag(abs(fft_z))
        m_list.append(m_x)
        m_list.append(m_y)
        m_list.append(m_z)

        norm_x = normalise(abs(fft_x))
        norm_y = normalise(abs(fft_y))
        norm_z = normalise(abs(fft_z))

        norm_list.append(norm_x)
        norm_list.append(norm_y)
        norm_list.append(norm_z)

    return t_list, m_list, norm_list


def calculate_fft_mag(r_list):
    t_list = []
    r = len(r_list) / 2
    for j in range(0, int(r)):
        t_list.append(math.sqrt(r_list[2 * j] * r_list[2 * j] + r_list[2 * j + 1] * r_list[2 * j + 1]))
    return t_list


def normalise(r_list):
    t_list = []
    sum_m = sum(r_list)
    t_list = [x / sum_m for x in r_list]
    return t_list


def calculate_entropy(r_list):
    fft_list, mag_list, norm_mag_list = calculate_fft(r_list)
    num_sensors = int(len(r_list) / 3)
    ent_x = 0
    ent_y = 0
    ent_z = 0
    t_list = []
    for i in range(0, num_sensors):
        for j in range(0, len(norm_mag_list[i])):
            ent_x = ent_x + norm_mag_list[3 * i][j] * math.log(norm_mag_list[3 * i][j], 2)
            ent_y += norm_mag_list[3 * i + 1][j] * math.log(norm_mag_list[3 * i + 1][j]) / math.log(2)
            ent_z += norm_mag_list[3 * i + 2][j] * math.log(norm_mag_list[3 * i + 2][j]) / math.log(2)

        ent_x *= -1
        ent_y *= -1
        ent_z *= -1
        t_list.append(ent_x)
        t_list.append(ent_y)
        t_list.append(ent_z)

    return t_list


def skewness(r_list):
    num_sensors = int(len(r_list) / 3)

    t_list = [0] * 3 * num_sensors

    for i in range(0, num_sensors):
        n_x = len(r_list[i * 0])
        temp_c = [0] * 3
        temp_b = [0] * 3
        temp_q = [0] * 3
        for j in range(0, len(r_list[i * 0])):
            temp_c[0] += math.pow(r_list[i * 3][j] - np.average(r_list[i * 3]), 3)
            temp_c[1] += math.pow(r_list[i * 3 + 1][j] - np.average(r_list[i * 3 + 1]), 3)
            temp_c[2] += math.pow(r_list[i * 3 + 2][j] - np.average(r_list[i * 3 + 2]), 3)

            temp_b[0] += math.pow(r_list[i * 3][j] - np.average(r_list[i * 3]), 2)
            temp_b[1] += math.pow(r_list[i * 3 + 1][j] - np.average(r_list[i * 3 + 1]), 2)
            temp_b[2] += math.pow(r_list[i * 3 + 2][j] - np.average(r_list[i * 3 + 2]), 2)

            temp_q[0] += math.pow(r_list[i * 3][j] - np.average(r_list[i * 3]), 4)
            temp_q[1] += math.pow(r_list[i * 3 + 1][j] - np.average(r_list[i * 3 + 1]), 4)
            temp_q[2] += math.pow(r_list[i * 3 + 2][j] - np.average(r_list[i * 3 + 2]), 4)

        t_list[3 * i] = (math.sqrt(n_x) * temp_c[0]) / (math.pow(temp_b[0], 1.5))
        t_list[3 * i + 1] = (math.sqrt(n_x) * temp_c[1]) / (math.pow(temp_b[1], 1.5))
        t_list[3 * i + 2] = (math.sqrt(n_x) * temp_c[2]) / (math.pow(temp_b[2], 1.5))
    
    return t_list

def kurtosis(r_list):
    num_sensors = int(len(r_list) / 3)

    k_list = [0] * 3 * num_sensors

    for i in range(0, num_sensors):
        n_x = len(r_list[i * 0])
        temp_c = [0] * 3
        temp_b = [0] * 3
        temp_q = [0] * 3
        for j in range(0, len(r_list[i * 0])):
            temp_c[0] += math.pow(r_list[i * 3][j] - np.average(r_list[i * 3]), 3)
            temp_c[1] += math.pow(r_list[i * 3 + 1][j] - np.average(r_list[i * 3 + 1]), 3)
            temp_c[2] += math.pow(r_list[i * 3 + 2][j] - np.average(r_list[i * 3 + 2]), 3)

            temp_b[0] += math.pow(r_list[i * 3][j] - np.average(r_list[i * 3]), 2)
            temp_b[1] += math.pow(r_list[i * 3 + 1][j] - np.average(r_list[i * 3 + 1]), 2)
            temp_b[2] += math.pow(r_list[i * 3 + 2][j] - np.average(r_list[i * 3 + 2]), 2)

            temp_q[0] += math.pow(r_list[i * 3][j] - np.average(r_list[i * 3]), 4)
            temp_q[1] += math.pow(r_list[i * 3 + 1][j] - np.average(r_list[i * 3 + 1]), 4)
            temp_q[2] += math.pow(r_list[i * 3 + 2][j] - np.average(r_list[i * 3 + 2]), 4)

        k_list[3 * i] = ((n_x * temp_q[0]) / (math.pow(temp_b[0], 2))) - 3
        k_list[3 * i + 1] = ((n_x * temp_q[1]) / (math.pow(temp_b[1], 2))) - 3
        k_list[3 * i + 2] = ((n_x * temp_q[2]) / (math.pow(temp_b[2], 2))) - 3

    return k_list


def calculate_quartiles(r_list):
    num_sensors = int(len(r_list) / 3)
    quartiles_x = []
    quartiles_y = []
    quartiles_z = []
    for i in range(0, num_sensors):
        iqr_x = np.quantile(r_list[3 * i], 0.75) - np.quantile(r_list[3 * i], 0.25)
        upper_x = np.quantile(r_list[3 * i], 0.75) + 1.5 * iqr_x
        lower_x = np.quantile(r_list[3 * i], 0.25) - 1.5 * iqr_x
        quartiles_x.extend(
            [np.quantile(r_list[3 * i], 0), np.quantile(r_list[3 * i], 0.25), np.quantile(r_list[3 * i], 0.5),
             np.quantile(r_list[3 * i], 0.75), np.quantile(r_list[3 * i], 1), iqr_x, upper_x, lower_x])
        iqr_y = np.quantile(r_list[3 * i + 1], 0.75) - np.quantile(r_list[3 * i + 1], 0.25)
        upper_y = np.quantile(r_list[3 * i + 1], 0.75) + 1.5 * iqr_y
        lower_y = np.quantile(r_list[3 * i + 1], 0.25) - 1.5 * iqr_y
        quartiles_y.extend([np.quantile(r_list[3 * i + 1], 0), np.quantile(r_list[3 * i + 1], 0.25),
                            np.quantile(r_list[3 * i + 1], 0.5), np.quantile(r_list[3 * i + 1], 0.75),
                            np.quantile(r_list[3 * i + 1], 1), iqr_y, upper_y, lower_y])
        iqr_z = np.quantile(r_list[3 * i + 2], 0.75) - np.quantile(r_list[3 * i + 2], 0.25)
        upper_z = np.quantile(r_list[3 * i + 2], 0.75) + 1.5 * iqr_z
        lower_z = np.quantile(r_list[3 * i + 2], 0.25) - 1.5 * iqr_z
        quartiles_z.extend([np.quantile(r_list[3 * i + 2], 0), np.quantile(r_list[3 * i + 2], 0.25),
                            np.quantile(r_list[3 * i + 2], 0.5), np.quantile(r_list[3 * i + 2], 0.75),
                            np.quantile(r_list[3 * i + 2], 1), iqr_z, upper_z, lower_z])

    return quartiles_x, quartiles_y, quartiles_z


def calculate_variance(r_list):
    num_sensors = int(len(r_list) / 3)
    t_list = []
    for i in range(0, num_sensors):
        t_list.append(np.var(r_list[3 * i]))
        t_list.append(np.var(r_list[3 * i + 1]))
        t_list.append(np.var(r_list[3 * i + 2]))
    return t_list


def coefficient_of_variation(r_list):
    num_sensors = int(len(r_list) / 3)
    t_list = []
    for i in range(0, num_sensors):
        t_list.append(variation(r_list[3 * i]))
        t_list.append(variation(r_list[3 * i + 1]))
        t_list.append(variation(r_list[3 * i + 2]))
    return t_list


def range_vector(r_list):
    num_sensors = int(len(r_list) / 3)
    t_list = []
    for i in range(0, num_sensors):
        t_list.append(max([abs(x) for x in r_list[3 * i]]))
        t_list.append(max([abs(x) for x in r_list[3 * i + 1]]))
        t_list.append(max([abs(x) for x in r_list[3 * i + 2]]))

    return t_list

def range_scalar(mag_list):
    num_sensors = len(mag_list)
    mag_t_list = []
    for i in range(0, num_sensors):
        mag_t_list.append(max([abs(x) for x in mag_list[i]]))
    return mag_t_list


def peaks(mag_list, band_passed):
    num_sensors = len(mag_list)
    peak_counter = [0] * num_sensors
    peaks = []
    peak_size = [0] * num_sensors
    peak_size_2 = [0] * num_sensors
    for i in range(0, num_sensors):
        trashold = 1.3
        if band_passed:
            trashold = 0.3
        previous_mag = 0
        max_mag = -200
        potential_peak = False
        counter = 0
        temp_peaks = []
        for j in range(0, len(mag_list[i])):
            value = mag_list[i][j]
            if value > trashold:
                # rising
                if value >= max_mag:
                    max_mag = value
                    potential_peak = True
                    temp_peaks.insert(counter, None)
                # falling
                elif value < max_mag:
                    # print("falling")
                    if potential_peak and (previous_mag > value):
                        prev_counter = counter - 1
                        if prev_counter != 0:
                            temp_peaks.insert(prev_counter, previous_mag)
                            peak_size[i] += previous_mag
                            peak_size_2[i] += previous_mag
                            peak_counter[i] += 1
                        temp_peaks.insert(counter, None)
                        potential_peak = False

                    else:
                        temp_peaks.insert(counter, None)
                # hit the bottom
                if (value > previous_mag) and (not potential_peak):
                    # print("hit the bottom")
                    potential_peak = True
                    temp_peaks.insert(counter, None)
                    max_mag = -200
            else:
                temp_peaks.insert(counter, None)

            previous_mag = value
            counter = counter + 1

        peaks.append(temp_peaks)
        if peak_counter[i] > 0:
            peak_size[i] = peak_size[i] / peak_counter[i]
            peak_size_2[i] = peak_size_2[i] / len(mag_list[i])
        else:
            peak_size[i] = 0

    return peaks, peak_counter, peak_size, peak_size_2


def mean_crossing_rate(r_list):
    num_signals = len(r_list)
    t_list = []
    for i in range(0, num_signals):
        signal_mean = np.mean(r_list[i])
        previous = 0
        changes = 0
        for j in range(0, len(r_list[i])):
            value = r_list[i][j] - signal_mean
            if previous != 0:
                if value * previous > 0:
                    changes += 1
            else:
                previous = value
        t_list.append(changes)

    return t_list


def signal_stats(r_list):
    return np.max(r_list), np.min(r_list), np.mean(r_list), np.median(r_list)


def signal_variance(r_list):
    return np.var(r_list)

def calc_average(snapshot):
    result_dict = {}
    if len(snapshot.temperature_objects) > 2:
        result_dict['temperature'] = np.average(snapshot.get_temp_objects())
    if len(snapshot.humidity_objects) > 2:
        result_dict['humidity'] = np.average(snapshot.get_humidity_objects())
    if len(snapshot.pressure_objects) > 2:
        result_dict['pressure'] = np.average(snapshot.get_pressure_objects())
    if len(snapshot.altitude_objects) > 2:
        result_dict['altitude'] = np.average(snapshot.get_altitude_objects())

    return result_dict


def calc_max(snapshot):
    result_dict = {}
    if len(snapshot.temperature_objects) > 2:
        result_dict['temperature'] = np.max(snapshot.get_temp_objects())
    if len(snapshot.humidity_objects) > 2:
        result_dict['humidity'] = np.max(snapshot.get_humidity_objects())
    if len(snapshot.pressure_objects) > 2:
        result_dict['pressure'] = np.max(snapshot.get_pressure_objects())
    if len(snapshot.altitude_objects) > 2:
        result_dict['altitude'] = np.max(snapshot.get_altitude_objects())

    return result_dict


def calc_min(snapshot):
    result_dict = {}
    if len(snapshot.temperature_objects) > 2:
        result_dict['temperature'] = np.min(snapshot.get_temp_objects())
    if len(snapshot.humidity_objects) > 2:
        result_dict['humidity'] = np.min(snapshot.get_humidity_objects())
    if len(snapshot.pressure_objects) > 2:
        result_dict['pressure'] = np.min(snapshot.get_pressure_objects())
    if len(snapshot.altitude_objects) > 2:
        result_dict['altitude'] = np.min(snapshot.get_altitude_objects())

    return result_dict
