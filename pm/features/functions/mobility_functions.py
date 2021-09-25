from ...utils import profile_lookup

def standing_seconds(timestamp, timestep, inputs):
    vals = next(iter(inputs.values()))

    return [(timestamp, timestep, sum(x[1] for x in vals if x[2] == 'Moving'))]

def cumulative_walking_time(timestamp, timestep, inputs):
    activity = next(iter(inputs.values()))

    walking_time = sum(tstep for _, tstep, a in activity if a == 'walk') / 60.0

    return [(timestamp, timestep, walking_time)]

def cumulative_walking_time_vs_prescribed(timestamp, timestep, inputs):
    length = inputs['feat_walking_time_cumulative'][0][2]
    prescribed_length = profile_lookup('maxWalkingCumulativeInMinutes')

    return [(timestamp, timestep, 'yes' if length > prescribed_length else 'no')]


def longest_walking_episode(timestamp, timestep, inputs):
    slack = 10  # how long can the difference between two consequiteve walking episodes
                # for them to be counted as the same episode
    activities = next(iter(inputs.values()))

    max_length = 0
    start = None
    current = None
    for ts, tstep, activity in activities:
        if activity == 'walk':
            if start is None:
                start = ts
            current = ts + tstep
        else:
            if activity != 'walk':
                if current is not None and ts - current > slack:
                    max_length = max(current - start, max_length)
                    start = None
                    current = None

    if current is not None:
        max_length = max(current - start, max_length)

    return [(timestamp, timestep, max_length / 60.0)]

def longest_walking_episode_vs_prescribed(timestamp, timestep, inputs):
    length = inputs['feat_walking_longest_episode_length'][0][2]
    prescribed_length = profile_lookup('maxWalkingEpisodeInMinutes')

    return [(timestamp, timestep, 'exceeded' if length > prescribed_length else 'in_limits')]


def walking_episode_qualitative(timestamp, timestep, inputs):
    minutes = inputs['feat_mobility_walking_longest_episode'][0][2]

    out = None

    if minutes > 0.25:
        out = 'normal_or_high'
    else:
        out = 'low'

    return [(timestamp, timestep, out)]

def cumulative_walking_time_qualitative(timestamp, timestep, inputs):
    minutes = inputs['feat_mobility_walking_duration'][0][2]

    out = None

    if minutes < 30:
        out = "low"
    elif minutes <= 90:
        out = "medium"
    else:
        out = "high"
    
    return [(timestamp, timestep, out)]
