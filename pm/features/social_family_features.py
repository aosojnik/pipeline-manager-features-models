from .functions import *
from .functions import chain as C, flat as F

FEATURES = {
    'feat_calls_count_family_relative': {
        'inputs': [
            'feat_calls_count_family_weekly',
            'feat_calls_count_family_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_calls_count_family_weekly': {
        'inputs': [
            ('app_daily_num_calls_family', '7d')
        ],
        'function': average,
        'window': '1d',
        'store': True
    },

    'feat_calls_count_family_total': {
        'inputs': [
            ('app_daily_num_calls_family', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'store': True
    },

    'feat_calls_duration_family_relative': {
        'inputs': [
            'feat_calls_count_family_weekly',
            'feat_calls_count_family_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_calls_duration_family_weekly': {
        'inputs': [
            ('app_daily_duration_calls_family', '7d')
        ],
        'function': average,
        'window': '1d',
        'store': True
    },

    'feat_calls_duration_family_total': {
        'inputs': [
            ('app_daily_duration_calls_family', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'store': True
    },

    'feat_visits_family_relative_past_week': {
        'inputs': [
            'feat_visits_family_count_weekly',
            'feat_visits_family_count_past_week',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_visits_family_relative': {
        'inputs': [
            'feat_visits_family_count_weekly',
            'feat_visits_family_count_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_visits_family_count_weekly': {
        'inputs': [
            ('app_daily_num_visits_family', '7d')
        ],
        'function': average,
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_visits_family_count_weekly_past_week': {
        'inputs': [
            ('app_daily_num_visits_family', '14d')
        ],
        'function': C(time_filter('14d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_visits_family_count_weekly_total': {
        'inputs': [
            ('app_daily_num_visits_family', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_family_relative_past_week': {
        'inputs': [
            'feat_outside_family_count_weekly',
            'feat_outside_family_count_past_week',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    # input
    'feat_outside_family_relative': {
        'inputs': [
            'feat_outside_family_count_weekly',
            'feat_outside_family_count_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True
    },

    'feat_outside_family_count_weekly': {
        'inputs': [
            ('app_daily_duration_outside_family', '7d')
        ],
        'function': average,
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_family_count_weekly_past_week': {
        'inputs': [
            ('app_daily_duration_outside_family', '14d')
        ],
        'function': C(time_filter('14d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_family_count_weekly_total': {
        'inputs': [
            ('app_daily_duration_outside_family', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_calls_count_family_weekly_vs_goal': {
        'inputs': [
            'feat_calls_count_family_weekly'
        ],
        'function': versus_goal('socialGoalTargets.Family.Calls'),
        'window': '1d',
        'store': True
    },

    'feat_visits_count_family_weekly_vs_goal': {
        'inputs': [
            'feat_visits_count_family_weekly'
        ],
        'function': versus_goal('socialGoalTargets.Family.Visits'),
        'window': '1d',
        'store': True
    },

    'feat_outside_count_family_weekly_vs_goal': {
        'inputs': [
            'feat_outside_family_count_weekly'
        ],
        'function': versus_goal('socialGoalTargets.Family.TogetherOutside'),
        'window': '1d',
        'store': True
    },

    'feat_social_activity_family_qualitative_lowest': {
        'inputs': [
            'feat_calls_count_family_weekly_vs_goal',
            'feat_visits_count_family_weekly_vs_goal',
            'feat_outside_count_family_weekly_vs_goal',
        ],
        'function': lowest_activity,
        'window': '1d',
        'store': True
    },

    'profile_social_invite_possible_family': {
        'inputs': [],
        'function': invite_possible_family,
        'window': '1d'
    }, 
}
