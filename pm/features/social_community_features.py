from .functions import *
from .functions import chain as C, flat as F

FEATURES = {
    'feat_community_habitual_weekly': {
        'inputs': [
            ('app_daily_presence_habitual_poi', '7d')
        ],
        'function': F(sum),
        'window': '1d', 
    },

    'feat_community_habitual_total': {
        'inputs': [
            ('app_daily_presence_habitual_poi', '56d')
        ],
        'function': C(time_filter('56d', '7d'), F(sum)),
        'window': '1d', 
    },

    'feat_community_nonhabitual_weekly': {
        'inputs': [
            ('app_daily_presence_nonhabitual_poi', '7d')
        ],
        'function': F(sum),
        'window': '1d', 
    },

    'feat_community_nonhabitual_total': {
        'inputs': [
            ('app_daily_presence_nonhabitual_poi', '56d')
        ],
        'function': C(time_filter('56d', '7d'), F(sum)),
        'window': '1d', 
    },

    'feat_community_habitual_weekly_vs_goal': {
        'inputs': [
            'feat_community_habitual_weekly'
        ],
        'function': versus_goal('socialGoalTargets.Community.HabitualPoi'),
        'window': '1d',
        'store': True
    },
    
    'feat_community_habitual_relative': {
        'inputs': [
            'feat_community_habitual_weekly',
            'feat_community_habitual_total'
        ],
        'function': relative_qualitative,
        'window': '1d',
        'store': True
    },

    'feat_community_nonhabitual': {
        'inputs': [
            'feat_community_nonhabitual_weekly',
        ],
        'function': nonhabitual_presence,
        'window': '1d',
        'store': True
    },

    'profile_social_planned_event_available': {
        'inputs': [],
        'function': event_available,
        'window': '1d',
    }
}
