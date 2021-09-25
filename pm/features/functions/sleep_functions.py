from .sleep_util import *

def sleep_magnitude_peaks(timestamp, timestep, inputs):
    strong_peaks = calculate_strong_peaks(inputs)

    peaks = []

    keys = sorted(strong_peaks.keys())
    for large in keys:
        peaks.append((large, "L"))
        for small in strong_peaks[large]:
            peaks.append((small, "S"))

    return [(timestamp, timestep, peaks)]

def sleep_state(timestamp, timestep, inputs):
    peaks = inputs['feat_bed_accel_magnitude_peaks'][0][2]

    if len(peaks) >= 2:
        state = []
        peak_time, peak_size = peaks[0]
        assert peak_time >= timestamp - timestep
        CURRENT = "out_of_bed"
        state.append((timestamp - timestep, peak_time, "out_of_bed"))
        for new_time, new_size in peaks[1:]:
            if new_size == peak_size == "L" or new_time - peak_time > 4 * 60 * 60:
                CURRENT = "out_of_bed"
                state.append((peak_time, new_time, "out_of_bed"))
            else:
                if new_time - peak_time < 15 * 60:
                    CURRENT = "in_bed"
                    state.append((peak_time, new_time, "in_bed"))
                else:
                    if CURRENT != "sleeping":
                        state.append((peak_time, peak_time + 15 * 60, "in_bed"))
                        state.append((peak_time + 15 * 60, new_time, "sleeping"))
                        CURRENT = "sleeping"
                    else:
                        state.append((peak_time, new_time, "sleeping"))
            peak_time, peak_size = new_time, new_size
        assert peak_time < timestamp
        state.append((peak_time, timestamp, "out_of_bed"))
        flat_states = []
        s = state.pop(0)
        while state:
            nxt = state.pop(0)
            if s[2] == nxt[2]:
                s = (s[0], nxt[1], s[2])
            else:
                flat_states.append(s)
                s = nxt
        flat_states.append(s)
        

    else:
        from ...data_handler import DataHandler

        DataHandler.warning(f"No peaks detected, assuming 'out_of_bed'. Recorded peaks: {peaks}")
        # If no peaks were detected, we assume the primary user was out of bed for the entire duration
        flat_states = [(timestamp - timestep, timestamp, "out_of_bed")]
    
    
    return [(timestamp, timestep, flat_states)]

def sleep_sensor_reliability(timestamp, timestep, inputs):
    peaks = inputs['feat_bed_accel_magnitude_peaks'][0][2]

    reliability = 0.75

    if len(peaks) < 2:
        reliability = 0
    
    return [(timestamp, timestep, reliability)]

def sleep_diary_reliability(timestamp, timestep, inputs):
    return [(timestamp, timestep, 0.75 if inputs['app_sleep_diary_morning'] else 0)]

def fuse_sleep_state(timestamp, timestep, inputs):
    sleep_state = sorted(inputs['feat_sleep_state'][0][2])

    activities = sorted(sum([v[0][2] for k, v in inputs.items() if k != "feat_sleep_state"], []))

    # merge activities
    if activities:
        flat_activities = []
        current_start, current_end = activities.pop(0)
        for start, end in activities:
            if start > current_end:
                flat_activities.append((current_start, current_end))
                current_start, current_end = start, end
            else:
                current_end = max(end, current_end)
        flat_activities.append((current_start, current_end))

        flat_activities.sort()

        fused_state = []
        activity = flat_activities.pop(0)
        fused_state.append((*activity, 'out_of_bed_active'))
        for s_start, s_end, s_state in sleep_state:
            if activity == None:
                fused_state.append((s_start, s_end, s_state))
            else:
                a_start, a_end = activity
                if s_end < a_start or s_start > a_end:
                    fused_state.append( (s_start, s_end, s_state) )
                elif s_start < a_start and s_end > a_start:
                    fused_state.append( (s_start, a_start, s_state) )
                elif s_start <= a_end and s_end > a_end:
                    fused_state.append( (a_end, s_end, s_state) )
                if s_end >= a_end:
                    activity = None if not flat_activities else flat_activities.pop(0)
                    if activity:
                        fused_state.append((*activity, 'out_of_bed_active'))
        if flat_activities:
            for activity in flat_activities:
                fused_state.append((*activity, 'out_of_bed_active'))

        fused_state.sort()
        return [(timestamp, timestep, fused_state)]              
    else:
        return [(timestamp, timestep, sleep_state)]

def sleep_latency(timestamp, timestep, inputs):
    sleep_state = inputs['fuse_sleep_state'][0][2]

    sleep_state_night = [(start, end, status) for start, end, status in sleep_state if (6 * 60 * 60 < (timestamp - start) % 24 * 60 * 60 < 22 * 60 * 60)]

    latency = 0
    for (first_start, first_end, first_state), (second_start, second_end, second_state) in zip(sleep_state_night, sleep_state_night[1:]):
        if first_state == "in_bed" and second_state == "sleeping":
            latency = (first_end - first_start) / 60
            break
    return [(timestamp, timestep, latency)]

def sleep_duration(timestamp, timestep, inputs):
    sleep_state = inputs['fuse_sleep_state'][0][2]
    duration = sum([(end - start) / 60 for start, end, status in sleep_state if status == "sleeping"])
    return [(timestamp, timestep, duration)]

def sleep_efficiency(timestamp, timestep, inputs):
    sleep_state = inputs['fuse_sleep_state'][0][2]
    sleep_state_night = [(start, end, status) for start, end, status in sleep_state if (6 * 60 * 60 < (timestamp - start) % 24 * 60 * 60 < 22 * 60 * 60)]

    sleep_duration = sum([(end - start) / 60 / 60 for start, end, status in sleep_state_night if status == "sleeping"])
    bed_duration = sum([(end - start) / 60 / 60 for start, end, status in sleep_state_night if status not in ["out_of_bed", "out_of_bed_active"]])

    # If bed_duration is 0, we expect a division by zero which defaults the feature value to None (i.e., take diary data)
    return [(timestamp, timestep, sleep_duration / bed_duration)]

def napped_minutes(timestamp, timestep, inputs):
    sleep_state = inputs['fuse_sleep_state'][0][2]

    nap_duration = sum([(end - start) / 60 for start, end, status in sleep_state if status == "sleeping" and not (6 * 60 * 60 < (timestamp - start) % 24 * 60 * 60 < 22 * 60 * 60)])

    return [(timestamp, timestep, nap_duration)]

def awake_minutes(timestamp, timestep, inputs):
    sleep_state = inputs['fuse_sleep_state'][0][2]

    awake_duration = sum(
        [
            (end - start) / 60 / 2
            for start, end, status in sleep_state
            if status == "in_bed" and (6 * 60 * 60 < (timestamp - start) % 24 * 60 * 60 < 22 * 60 * 60)
        ]
    )

    return [(timestamp, timestep, awake_duration)]


def sleep_temperature(timestamp, timestep, inputs):
    sleep_state = inputs['fuse_sleep_state'][0][2]

    if not sleep_state:
        return [(timestamp, timestep, float('nan'))]
    sleep_state_night = [(start, end, status) for start, end, status in sleep_state if status == "sleeping" and (6 * 60 * 60 < (timestamp - start) % 24 * 60 * 60 < 22 * 60 * 60)]

    temperatures = []
    for start, end, _ in sleep_state_night:
        temperatures += [x[2] for x in inputs['sens_amb_1_temp_raw'] if start <= x[0] <= end]
    if temperatures:
        return [(timestamp, timestep, (sum(temperatures) / len(temperatures)) - 17)]
    else:
        return [(timestamp, timestep, float('nan'))]

def fuse_sleep_duration(timestamp, timestep, inputs):
    duration_sensor = inputs['feat_sleep_duration'][0][2]
    duration_diary = None

    if inputs['app_sleep_diary_morning']:
        sleep_start_diary = ensure_datetime(inputs['app_sleep_diary_morning'][0][2]['WentToBedAt'])
        sleep_end_diary = ensure_datetime(inputs['app_sleep_diary_morning'][0][2]['WokeUpAt'])
        sleep_delay_diary = inputs['app_sleep_diary_morning'][0][2]['MinutesUntilAsleep']

        duration_diary = (sleep_end_diary - sleep_start_diary).seconds / 60 - sleep_delay_diary

    reliability_sensor = inputs['feat_sleep_sensor_reliability'][0][2]
    reliability_diary = inputs['feat_sleep_diary_reliability'][0][2]

    fused = fuse_with_reliability((reliability_diary, duration_diary), (reliability_sensor, duration_sensor))

    return [(timestamp, timestep, fused)]


def fuse_sleep_efficiency(timestamp, timestep, inputs):
    efficiency_sensor = inputs['feat_sleep_efficiency'][0][2]
    efficiency_diary = None

    if inputs['app_sleep_diary_morning']:
        bed_start_diary = ensure_datetime(inputs['app_sleep_diary_morning'][0][2]['WentToBedAt'])
        sleep_end_diary = ensure_datetime(inputs['app_sleep_diary_morning'][0][2]['WokeUpAt'])
        bed_end_diary = ensure_datetime(inputs['app_sleep_diary_morning'][0][2]['LeftBedAt'])
        sleep_delay_diary = inputs['app_sleep_diary_morning'][0][2]['MinutesUntilAsleep']

        efficiency_diary = ((sleep_end_diary - bed_start_diary).seconds / 60 - sleep_delay_diary) / ((bed_end_diary - bed_start_diary).seconds / 60)

    reliability_sensor = inputs['feat_sleep_sensor_reliability'][0][2]
    reliability_diary = inputs['feat_sleep_diary_reliability'][0][2]

    fused = fuse_with_reliability((reliability_diary, efficiency_diary), (reliability_sensor, efficiency_sensor))

    return [(timestamp, timestep, fused)]


def fuse_sleep_latency(timestamp, timestep, inputs):
    latency_sensor = inputs['feat_sleep_latency'][0][2]
    latency_diary = None
    
    if inputs['app_sleep_diary_morning']:
        latency_diary = inputs['app_sleep_diary_morning'][0][2]['MinutesUntilAsleep']

    reliability_sensor = inputs['feat_sleep_sensor_reliability'][0][2]
    reliability_diary = inputs['feat_sleep_diary_reliability'][0][2]

    fused = fuse_with_reliability((reliability_diary, latency_diary), (reliability_sensor, latency_sensor))

    return [(timestamp, timestep, fused)]


def fuse_awake_minutes(timestamp, timestep, inputs):
    awake_minutes_sensor = inputs['feat_sleep_awake_minutes'][0][2]
    awake_minutes_diary = None
    
    if inputs['app_sleep_diary_morning']:
        sleep_end_diary = ensure_datetime(inputs['app_sleep_diary_morning'][0][2]['WokeUpAt'])
        bed_end_diary = ensure_datetime(inputs['app_sleep_diary_morning'][0][2]['LeftBedAt'])
        awake_minutes_diary = (bed_end_diary - sleep_end_diary).seconds // 60

    reliability_sensor = inputs['feat_sleep_sensor_reliability'][0][2]
    reliability_diary = inputs['feat_sleep_diary_reliability'][0][2]

    fused = fuse_with_reliability((reliability_diary, awake_minutes_diary), (reliability_sensor, awake_minutes_sensor))

    return [(timestamp, timestep, fused)]


# -----------------------------------------
# - QUALITATIVE FUNCTIONS FOR DEXI INPUTS -
# -----------------------------------------


def sleep_subjective_quality_qualitative(timestamp, timestep, inputs):
    # Values:
    # 0 = Very good
    # 1 = Fairly good
    # 2 = Fairly bad
    # 3 = Very bad
    sleep_quality_reported = inputs['app_sleep_diary_morning'][0][2]['DidYouSleepWell']
    return [(timestamp, timestep, str(sleep_quality_reported))]


def sleep_subjective_quality_qualitative_weekly(timestamp, timestep, inputs):
    # Values:
    # 0 = Very good
    # 1 = Fairly good
    # 2 = Fairly bad
    # 3 = Very bad
    s = sum(v['DidYouSleepWell'] for t, s, v in inputs['app_sleep_diary_morning'])
    n = len(inputs['app_sleep_diary_morning'])
    sleep_quality_reported = s / n
    return [(timestamp, timestep, str(round(sleep_quality_reported)))]


def sleep_napped_during_day(timestamp, timestep, inputs):
    mins = inputs['situ_sleep_napped_minutes'][0][2]
    return [(timestamp, timestep, str(int(mins > 0)))]


def sleep_napped_during_day_weekly(timestamp, timestep, inputs):
    napped_days = sum(int(n) for t, s, n in inputs['situ_sleep_napped_during_day'])
    return [(timestamp, timestep, str(int(napped_days >= 3)))]


def sleep_latency_qualitative(timestamp, timestep, inputs):
    num_latency = inputs['fuse_sleep_latency'][0][2]

    if (num_latency < 15):
        result = 0
    elif (num_latency >= 15) and (num_latency < 30):
        result = 1
    elif (num_latency >= 30) and (num_latency < 60):
        result = 2
    elif (num_latency > 60):
        result = 3
    return [(timestamp, timestep, str(result))]


def sleep_latency_qualitative_weekly(timestamp, timestep, inputs):
    s = sum(v for t, s, v in inputs['fuse_sleep_latency'] if v)
    n = sum(1 for t, s, v in inputs['fuse_sleep_latency'] if v)

    num_latency = s / n
  
    if (num_latency < 15):
        result = 0
    elif (num_latency >= 15) and (num_latency < 30):
        result = 1
    elif (num_latency >= 30) and (num_latency < 60):
        result = 2
    elif (num_latency > 60):
        result = 3
    return [(timestamp, timestep, str(result))]


def sleep_duration_qualitative(timestamp, timestep, inputs):
    # inputs is a dict that contains key 'feat_sleep_duration'
    # timestamp is just to be passed on in this case
    # timestep is just to be passed on in this case
    # inputs['feat_sleep_duration'] is a list of triplots (timestamp, timestep, value)
    # there should be only one item in this list in 24h time
    sleep_minutes = inputs['fuse_sleep_duration'][0][2]   # we expect sleep duration in minutes here

    if (sleep_minutes >= 420):
        result = 0
    elif ((sleep_minutes >= 360) and (sleep_minutes < 420)):
        result = 1
    elif ((sleep_minutes >= 300) and (sleep_minutes < 360)):
        result = 2
    elif (sleep_minutes < 300):
        result = 3
    return [(timestamp, timestep, str(result))]


def sleep_efficiency_qualitative(timestamp, timestep, inputs):
    sleep_efficiency = inputs['fuse_sleep_efficiency'][0][2]
    if (sleep_efficiency >= 0.85):
        result = 0
    elif ((sleep_efficiency >= 0.75) and (sleep_efficiency < 0.85)):
        result = 1
    elif ((sleep_efficiency >= 0.65) and (sleep_efficiency < 0.75)):
        result = 2
    elif (sleep_efficiency < 0.65):
        result = 3
    return [(timestamp, timestep, str(result))]

def sleep_efficiency_qualitative_weekly(timestamp, timestep, inputs):
    s = sum(v for t, s, v in inputs['fuse_sleep_efficiency'])
    n = sum(1 for t, s, v in inputs['fuse_sleep_efficiency'])

    sleep_efficiency = s / n

    if (sleep_efficiency >= 0.85):
        result = 0
    elif ((sleep_efficiency >= 0.75) and (sleep_efficiency < 0.85)):
        result = 1
    elif ((sleep_efficiency >= 0.65) and (sleep_efficiency < 0.75)):
        result = 2
    elif (sleep_efficiency < 0.65):
        result = 3
    return [(timestamp, timestep, str(result))]  

def sleep_efficiency_qualitative(timestamp, timestep, inputs):
    sleep_efficiency = inputs['fuse_sleep_efficiency'][0][2]

    if (sleep_efficiency >= 0.85):
        result = 0
    elif ((sleep_efficiency >= 0.75) and (sleep_efficiency < 0.85)):
        result = 1
    elif ((sleep_efficiency >= 0.65) and (sleep_efficiency < 0.75)):
        result = 2
    elif (sleep_efficiency < 0.65):
        result = 3
    return [(timestamp, timestep, str(result))]    

def sleep_disturbance_type(timestamp, timestep, inputs):
    disturbance = inputs['app_sleep_diary_morning'][0][2]['DidYouHaveTroubleSleeping']

    DISTURBANCE_MAPPING = {
        0: 'none', # SleepXMinutes
        1: 'none', # WakeUp
        2: 'bathroom', # UseBathroom
        3: 'medical', # BreatheProblem
        4: 'medical', # CoughOrSnore
        5: 'temperature', # TooHot
        6: 'none', # TooCold
        7: 'none', # BadDreams
        8: 'medical', # Pain
        9: 'none' # NoProblems
    }

    return [(timestamp, timestep, DISTURBANCE_MAPPING[disturbance])]

def sleep_disturbance_type_weekly(timestamp, timestep, inputs):
    DISTURBANCES = ['medical', 'temperature', 'bathroom', 'none']

    occurences, index = max((sum(1 for _, _, d in inputs['situ_sleep_disturbance_type'] if d == typ), -i) for i, typ in enumerate(DISTURBANCES))

    return [(timestamp, timestep, DISTURBANCES[-index])]

def sleep_number_disturbances(timestamp, timestep, inputs):
    disturbance_n = inputs['app_sleep_diary_morning'][0][2]['HowOftenDidYouWake']

    DISTURBANCE_N_MAPPING = {
        0: '0', # Never
        1: '1-2', # OneTwoTimes
        2: '3-5', # ThreeFiveTimes
        3: '5+', # MoreThanFive
    }

    return [(timestamp, timestep, DISTURBANCE_N_MAPPING[disturbance_n])]

def sleep_disturbances_qualitative(timestamp, timestep, inputs):
    values = [(ts, d['HowOftenDidYouWake']) for ts, _, d in inputs['app_sleep_diary_morning']]
    disturbs_30days = sum(v for ts, v in values) 
    disturbs_7days = sum(v for ts, v in values if abs(ts - timestamp) <= 604800000)
    
    if (disturbs_30days == 0):
        result = 0
    elif (disturbs_7days < 1) and (disturbs_30days > 0):
        result = 1
    elif (disturbs_7days >=1) and (disturbs_7days <=2):
        result = 2
    elif (disturbs_7days > 2):
        result = 3

    return [(timestamp, timestep, result)]


def sleep_medication_qualitative(timestamp, timestep, inputs):
    medication_used = inputs['app_sleep_diary_morning'][0][2]['DidYouTakeAnyMedicineToSleep']
    if medication_used:
        result = 3
    else:
        result = 0
    return [(timestamp, timestep, result)]


def sleep_daytime_disfunction_qualitative(timestamp, timestep, inputs):
    problem_awake = inputs['app_sleep_diary_evening'][0][2]['TroubleStayingAwake']
    problem_enthusiasm = inputs['app_sleep_diary_evening'][0][2]['EnthusiasmProblems']
    s = problem_awake + problem_enthusiasm
    result = s * 1.5
    return [(timestamp, timestep, result)]


def sleep_overall_sleep_quality(timestamp, timestep, inputs):
    subj_qual = float(inputs['situ_sleep_subjective_quality_qualitative'][0][2])
    latency = float(inputs['situ_sleep_latency_qualitative'][0][2])
    duration = float(inputs['situ_sleep_duration_qualitative'][0][2])
    efficiency = float(inputs['situ_sleep_efficiency_qualitative'][0][2])
    disturbances = float(inputs['situ_sleep_disturbances_qualitative'][0][2])
    medication = float(inputs['situ_sleep_medication_qualitative'][0][2])
    daytime_disfunction = float(inputs['situ_sleep_daytime_disfunction_qualitative'][0][2])
    result = (subj_qual + latency + duration + efficiency + disturbances + medication + daytime_disfunction)/7.0
    return [(timestamp, timestep, result)]



def sleep_coaching_reliability(timestamp, timestep, inputs):
    sensor_reliability = inputs['feat_sleep_sensor_reliability'][0][2]
    diary_reliability = inputs['feat_sleep_diary_reliability'][0][2]

    return [(timestamp, timestep, max(sensor_reliability, diary_reliability))]


# WEEKLY AGGREGATIONS

def activity_physical_weekly(timestamp, timestep, inputs):
    s = sum(int(v) for t, s, v in inputs['situ_activity_physical'] if v)
    n = sum(1 for t, s, v in inputs['situ_activity_physical'] if v)

    return [(timestamp, timestep, str(round(s / n)))]