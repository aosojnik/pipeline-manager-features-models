from .functions import *
from .functions import chain as C, flat as F

FEATURES = {
    # input
    'feat_calls_count_friends_relative': {
        'inputs': [
            'feat_calls_count_friends_weekly',
            'feat_calls_count_friends_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_calls_count_friends_weekly': {
        'inputs': [
            ('app_daily_num_calls_friends', '7d')
        ],
        'function': average,
        'window': '1d',
        'store': True
    },

    'feat_calls_count_friends_total': {
        'inputs': [
            ('app_daily_num_calls_friends', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'store': True
    },

    'feat_calls_duration_friends_relative': {
        'inputs': [
            'feat_calls_count_friends_weekly',
            'feat_calls_count_friends_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_calls_duration_friends_weekly': {
        'inputs': [
            ('app_daily_duration_calls_friends', '7d')
        ],
        'function': average,
        'window': '1d',
        'store': True
    },

    'feat_calls_duration_friends_total': {
        'inputs': [
            ('app_daily_duration_calls_friends', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'store': True
    },

    'feat_visits_friends_relative_past_week': {
        'inputs': [
            'feat_visits_friends_count_weekly',
            'feat_visits_friends_count_past_week',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_visits_friends_relative': {
        'inputs': [
            'feat_visits_friends_count_weekly',
            'feat_visits_friends_count_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_visits_friends_count_weekly': {
        'inputs': [
            ('app_daily_num_visits_friends', '7d')
        ],
        'function': average,
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_visits_friends_count_weekly_past_week': {
        'inputs': [
            ('app_daily_num_visits_friends', '14d')
        ],
        'function': C(time_filter('14d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_visits_friends_count_weekly_total': {
        'inputs': [
            ('app_daily_num_visits_friends', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_friends_relative_past_week': {
        'inputs': [
            'feat_outside_friends_count_weekly',
            'feat_outside_friends_count_past_week',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True,
        'default': 'stable'
    },

    'feat_outside_friends_relative': {
        'inputs': [
            'feat_outside_friends_count_weekly',
            'feat_outside_friends_count_total',
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True
    },

    'feat_outside_friends_count_weekly': {
        'inputs': [
            ('app_daily_duration_outside_friends', '7d')
        ],
        'function': average,
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_friends_count_weekly_past_week': {
        'inputs': [
            ('app_daily_duration_outside_friends', '14d')
        ],
        'function': C(time_filter('14d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_outside_friends_count_weekly_total': {
        'inputs': [
            ('app_daily_duration_outside_friends', '56d')
        ],
        'function': C(time_filter('56d', '7d'), average),
        'window': '1d',
        'default': 0,
        'store': True
    },

    'feat_calls_count_friends_weekly_vs_goal': {
        'inputs': [
            'feat_calls_count_friends_weekly'
        ],
        'function': versus_goal('socialGoalTargets.Friends.Calls'),
        'window': '1d',
        'store': True
    },

    'feat_visits_count_friends_weekly_vs_goal': {
        'inputs': [
            'feat_visits_count_friends_weekly'
        ],
        'function': versus_goal('socialGoalTargets.Friends.Visits'),
        'window': '1d',
        'store': True
    },

    'feat_outside_count_friends_weekly_vs_goal': {
        'inputs': [
            'feat_outside_friends_count_weekly'
        ],
        'function': versus_goal('socialGoalTargets.Friends.TogetherOutside'),
        'window': '1d',
        'store': True
    },

    'feat_social_activity_friends_qualitative_lowest': {
        'inputs': [
            'feat_calls_count_friends_weekly_vs_goal',
            'feat_visits_count_friends_weekly_vs_goal',
            'feat_outside_count_friends_weekly_vs_goal',
        ],
        'function': lowest_activity,
        'window': '1d',
        'store': True
    },

    'profile_social_invite_possible_friends': {
        'inputs': [],
        'function': invite_possible_friends,
        'window': '1d'
    },
}
