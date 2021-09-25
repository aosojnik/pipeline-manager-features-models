from .functions import *
from .functions import chain as C, flat as F

FEATURES = {
    'feat_calls_count_total_relative': {
        'inputs': [
            'feat_calls_count_total_weekly',
            'feat_calls_count_total_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_calls_count_total_weekly': {
        'inputs': [
            ('app_daily_num_calls_total', '7d')
        ],
        'function': average,
        'window': '1d',
        'store': True
    },

    'feat_calls_count_total_total': {
        'inputs': [
            ('app_daily_num_calls_total', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'store': True
    },

    'feat_calls_duration_total_relative': {
        'inputs': [
            'feat_calls_count_total_weekly',
            'feat_calls_count_total_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_calls_duration_total_weekly': {
        'inputs': [
            ('app_daily_duration_calls_total', '7d')
        ],
        'function': average,
        'window': '1d',
        'store': True
    },

    'feat_calls_duration_total_total': {
        'inputs': [
            ('app_daily_duration_calls_total', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'store': True
    },

    'feat_visits_total_relative_past_week': {
        'inputs': [
            'feat_visits_total_count_weekly',
            'feat_visits_total_count_past_week',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_visits_total_relative': {
        'inputs': [
            'feat_visits_total_count_weekly',
            'feat_visits_total_count_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_visits_total_count_weekly': {
        'inputs': [
            ('app_daily_num_visits_total', '7d')
        ],
        'function': average,
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_visits_total_count_weekly_past_week': {
        'inputs': [
            ('app_daily_num_visits_total', '14d')
        ],
        'function': C(time_filter('14d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_visits_total_count_weekly_total': {
        'inputs': [
            ('app_daily_num_visits_total', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_total_relative_past_week': {
        'inputs': [
            'feat_outside_total_count_weekly',
            'feat_outside_total_count_past_week',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_outside_total_relative': {
        'inputs': [
            'feat_outside_total_count_weekly',
            'feat_outside_total_count_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True
    },

    'feat_outside_total_count_weekly': {
        'inputs': [
            ('app_daily_duration_outside_total', '7d')
        ],
        'function': average,
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_total_count_weekly_past_week': {
        'inputs': [
            ('app_daily_duration_outside_total', '14d')
        ],
        'function': C(time_filter('14d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_total_count_weekly_total': {
        'inputs': [
            ('app_daily_duration_outside_total', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_calls_count_total_weekly_vs_goal': {
        'inputs': [
            'feat_calls_count_total_weekly'
        ],
        'function': versus_goal('socialGoalTargets.General.Calls'),
        'window': '1d',
        'store': True
    },

    'feat_visits_count_total_weekly_vs_goal': {
        'inputs': [
            'feat_visits_count_total_weekly'
        ],
        'function': versus_goal('socialGoalTargets.General.Visits'),
        'window': '1d',
        'store': True
    },

    'feat_outside_count_total_weekly_vs_goal': {
        'inputs': [
            'feat_outside_total_count_weekly'
        ],
        'function': versus_goal('socialGoalTargets.General.Outside'),
        'window': '1d',
        'store': True
    },

    'feat_social_activity_total_qualitative_lowest': {
        'inputs': [
            'feat_calls_count_total_weekly_vs_goal',
            'feat_visits_count_total_weekly_vs_goal',
            'feat_outside_count_total_weekly_vs_goal',
        ],
        'function': lowest_activity,
        'window': '1d',
        'store': True
    },

    'profile_social_invite_possible_general': {
        'inputs': [],
        'function': invite_possible,
        'window': '1d'
    },
}
