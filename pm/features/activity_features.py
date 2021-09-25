from .functions import *
from .functions import chain as C, flat as F

FEATURES = {
    'feat_activity_oven': {
        'inputs': [
            'sens_power_event_f1_oven',
            'sens_power_event_f2_oven',
            'sens_power_event_f3_oven'
        ],
        'function': activity_calculator(1800),
        'window': '24h',
        'store': True
    },

    'feat_activity_stove': {
        'inputs': [
            'sens_power_event_f1_stove',
            'sens_power_event_f2_stove',
            'sens_power_event_f3_stove'
        ],
        'function': activity_calculator(1800),
        'window': '24h',
        'store': True
    },

    'feat_activity_cooking_daily': {
        'inputs': [
            'feat_activity_oven',
            'feat_activity_stove'
        ],
        'function': count_activity_entries,
        'window': '24h',
        'store': True
    },

    'feat_activity_cooking_weekly_average': {
        'inputs': [
            ('feat_activity_cooking_daily', '7d')
        ],
        'function': average,
        'window': '1d',
        'store': True
    },

    'feat_activity_cooking_weekly_median': {
        'inputs': [
            ('feat_activity_cooking_daily', '7d')
        ],
        'function': median,
        'window': '1d',
        'default': 1,
        'store': True
    },

    'feat_cooking_recorded': {
        'inputs': [
            'feat_activity_cooking_weekly_average'
        ],
        'function': cooking_qualitative,
        'window': '1d',
        'store': True
    },

    'feat_cooking_predicted': {
        'inputs': [
            ('feat_activity_cooking_daily', '28d')
        ],
        'function': C(time_filter('28d', '7d'), average, cooking_qualitative),
        'window': '1d',
        'store': True
    },

    'feat_outside_time_weekly': {
        'inputs': [
            ('app_daily_duration_outside_total', '7d')
        ],
        'function': average,
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_time_total': {
        'inputs': [
            ('app_daily_duration_outside_total', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_activity_outside_recorded': {
        'inputs': [
            'feat_outside_time_weekly'
        ],
        'function': time_outside_qualitative,
        'window': '1d',
    },

    'feat_activity_outside_predicted': {
        'inputs': [
            'feat_outside_time_total'
        ],
        'function': time_outside_qualitative,
        'window': '1d',
    },

}