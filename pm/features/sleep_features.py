from .functions import *
from .functions import chain as C, flat as F

FEATURES = {
    'fuse_bed_accel': {
        'inputs': [
            'sens_bed_accel_amb',
            'sens_bed_accel_egw',
            'sens_bed_accel_app'
        ],
        'function': flat_fuse,
        'window': '',
    },

    'feat_bed_accel_magnitude_max': {
        'inputs': [
            ('feat_bed_accel_magnitude', '5s')
        ],
       'function': F(max),
       'window': '5s'
    },

    'feat_bed_accel_magnitude': {
        'inputs': [
            'fuse_bed_accel'
        ],
        'function': magnitude,
        'window': '',
    },

    'feat_bed_accel_magnitude_peaks': {
        'inputs': [
            'feat_bed_accel_magnitude'
        ],
        'function': sleep_magnitude_peaks,
        'window': '24h',
        'default': [],
        'store': True
    },

    'feat_sleep_state': {
        'inputs': [
            'feat_bed_accel_magnitude_peaks'
        ],
        'function': sleep_state,
        'window': '24h',
        'default': None,
        'store': True
    },

    'feat_sleep_sensor_reliability': {
        'inputs': [
            'feat_bed_accel_magnitude_peaks'
        ],
        'function': sleep_sensor_reliability,
        'window': '24h',
        'store': True,
        'default': 0
    },

    'fuse_sleep_state': {
        'inputs': [
            'feat_sleep_state',
            'feat_activity_stove',
            'feat_activity_oven',
        ],
        'function': fuse_sleep_state,
        'window': '24h',
        'default': None,
        'store': True
    },

    'feat_sleep_duration': {
        'inputs': [
            'fuse_sleep_state'
        ],
        'function': sleep_duration,
        'window': '24h',
        'store': True,
        'default': None
    },

    'feat_sleep_latency': {
        'inputs': [
            'fuse_sleep_state'
        ],
        'function': sleep_latency,
        'window': '24h',
        'store': True,
        'default': None,
    },

    'feat_sleep_efficiency': {
        'inputs': [
            'fuse_sleep_state'
        ],
        'function': sleep_efficiency,
        'window': '24h',
        'store': True,
        'default': None
    },

    'feat_sleep_diary_reliability': {
        'inputs': [
            'app_sleep_diary_morning'
        ],
        'function': sleep_diary_reliability,
        'window': '24h',
        'default': 0
    },

    'fuse_sleep_latency': {
        'inputs': [
            'feat_sleep_latency', 
            'app_sleep_diary_morning',
            'feat_sleep_sensor_reliability',
            'feat_sleep_diary_reliability',
        ],
        'function': fuse_sleep_latency,
        'window': '24h',
        'store': True
    },

    'fuse_sleep_efficiency': {
        'inputs': [
            'feat_sleep_efficiency', 
            'app_sleep_diary_morning',
            'feat_sleep_sensor_reliability',
            'feat_sleep_diary_reliability',
        ],
        'function': fuse_sleep_efficiency,
        'window': '24h',
        'store': True
    },

    'fuse_sleep_duration': {
        'inputs': [
            'feat_sleep_duration', 
            'app_sleep_diary_morning',
            'feat_sleep_sensor_reliability',
            'feat_sleep_diary_reliability',
        ],
        'function': fuse_sleep_duration,
        'window': '24h',
        'store': True
    },

    'situ_sleep_subjective_quality_qualitative': {
        'inputs': [
            'app_sleep_diary_morning' # DidYouSleepWell
        ],
        'function': sleep_subjective_quality_qualitative,
        'window': '24h',
        'store': True,
        'default': '0'
    },

    'situ_sleep_subjective_quality_qualitative_weekly': {
        'inputs': [
            ('app_sleep_diary_morning', '7d') # DidYouSleepWell
        ],
        'function': sleep_subjective_quality_qualitative_weekly,
        'window': '24h',
        'store': True,
        'default': '0'
    },

    'situ_sleep_latency_qualitative': {
        'inputs': [
            'fuse_sleep_latency'
        ],
        'function': sleep_latency_qualitative,
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_sleep_latency_qualitative_weekly': {
        'inputs': [
            ('fuse_sleep_latency', '7d')
        ],
        'function': sleep_latency_qualitative_weekly,
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_sleep_napped_minutes': {
        'inputs': [
            'fuse_sleep_state'
        ],
        'function': napped_minutes,
        'default': '>0',
        'window': '24h',
        'store': True
    },

    'situ_sleep_napped_during_day': {
        'inputs': [
            'situ_sleep_napped_minutes'
        ],
        'function': sleep_napped_during_day,
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_sleep_napped_during_day_weekly': {
        'inputs': [
            ('situ_sleep_napped_during_day', '7d')
        ],
        'function': sleep_napped_during_day_weekly,
        'default': '0',
        'window': '24h',
        'store': True
    },

    'feat_sleep_temperature': {
        'inputs': [
            'fuse_sleep_state',
            'sens_amb_1_temp_raw'
        ],
        'function': sleep_temperature,
        'window': '24h',
        'store': True
    },

    'feat_sleep_awake_minutes': {
        'inputs': [
            'fuse_sleep_state',
        ],
        'function': awake_minutes,
        'default': None,
        'window': '24h',
        'store': True
    },

    'situ_sleep_awake_minutes': {
        'inputs': [
            'feat_sleep_awake_minutes',
            'app_sleep_diary_morning'
        ],
        'function': fuse_awake_minutes,
        'default': 0,
        'window': '24h',
        'store': True
    },

    'situ_sleep_efficiency_qualitative': {
        'inputs': [
            'fuse_sleep_efficiency'
        ],
        'function': sleep_efficiency_qualitative,
        'window': '24h',
        'default': '0',
        'store': True
    },


    'situ_sleep_efficiency_qualitative_weekly': {
        'inputs': [
            ('fuse_sleep_efficiency', '7d')
        ],
        'function': sleep_efficiency_qualitative_weekly,
        'window': '24h',
        'default': '0',
        'store': True
    },

    'situ_sleep_duration_qualitative': {
        'inputs': [
            'fuse_sleep_duration'
        ], 
        'function': sleep_duration_qualitative, 
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_sleep_number_disturbances': {
        'inputs': [
            'app_sleep_diary_morning', # HowOftenDidYouWake
        ],
        'function': sleep_number_disturbances,
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_sleep_disturbance_type': {
        'inputs': [
            'app_sleep_diary_morning', # DidYouHaveTroubleSleeping
        ],
        'function': sleep_disturbance_type,
        'default': 'no_data',
        'window': '24h',
        'store': True
    },


    'situ_sleep_disturbance_type_weekly': {
        'inputs': [
            ('situ_sleep_disturbance_type', '7d')
        ],
        'function': sleep_disturbance_type_weekly,
        'default': 'none',
        'window': '24h',
        'store': True
    },

    'situ_sleep_disturbances_qualitative': {
        'inputs': [
            ('app_sleep_diary_morning', '30d'), # HowOftenDidYouWake
        ],
        'function': sleep_disturbances_qualitative,
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_sleep_medication_qualitative': {
        'inputs': [
            'app_sleep_diary_morning' # DidYouTakeAnyMedicineToSleep
        ],
        'function': sleep_medication_qualitative,
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_activity_physical': {
        'inputs': [], # TODO
        'function': constant('0'),
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_activity_physical_weekly': {
        'inputs': [
            ('situ_activity_physical', '7d')
        ],
        'function': activity_physical_weekly,
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_sleep_daytime_disfunction_qualitative': {
        'inputs': [
            'app_sleep_diary_evening' # TroubleStayingAwake & EnthusiasmProblems
        ],
        'function': sleep_daytime_disfunction_qualitative,
        'default': '0',
        'window': '24h',
        'store': True
    },

    'situ_sleep_overall_sleep_quality': {   # The topmost concept (numeric, for use in the App - overview for PU)
        'inputs': [
            'situ_sleep_subjective_quality_qualitative',
            'situ_sleep_latency_qualitative',
            'situ_sleep_duration_qualitative',
            'situ_sleep_efficiency_qualitative',
            'situ_sleep_disturbances_qualitative',
            'situ_sleep_medication_qualitative',
            'situ_sleep_daytime_disfunction_qualitative'
        ],
        'function': sleep_overall_sleep_quality,
        'default': '0',
        'window': '24h',
        'store': True,
    },

    'situ_sleep_maximum_sleep_quality': {   # Maximum value for 'situ_sleep_overall_sleep_quality', used for rendering
        'inputs': [],
        'function': constant('3'),
        'window': '24h',
    },

    'situ_sleep_coaching_reliability': {
        'inputs': [
            'feat_sleep_sensor_reliability',
            'feat_sleep_diary_reliability'
        ],
        'window': '24h',
        'function': sleep_coaching_reliability,
        'store': True
    },

    'situ_sleep_coaching_reliability_weekly': {
        'inputs': [
            ('situ_sleep_coaching_reliability', '7d')
        ],
        'window': '24h',
        'function': average,
        'store': True
    },
}
