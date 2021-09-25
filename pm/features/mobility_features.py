from .functions import *
from .functions import chain as C, flat as F, mapper as M

import tsfresh.feature_extraction.feature_calculators as fc
import numpy as np

FEATURES = {
    'fuse_belt_accel': {
        'inputs': [
            'sens_belt_accel_amb',
            'sens_belt_accel_egw',
            'sens_belt_accel_app'
        ],
        'function': flat_fuse,
        'window': '',
    },

    'feat_belt_accel_magnitude': {
        'inputs': [
            'fuse_belt_accel',
        ],
       'function': magnitude,
       'window': ''
    },

    'feat_mobility_label_mode': {
        'inputs': [
            'feat_mobility_label'
        ],
        'function': mode,
        'window': '5s',
        'default': 'NO_LABEL'
    },

    'feat_belt_accel_magnitude_approx_entropy_2_0.5': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.approximate_entropy, 2, 0.5)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_change_quantiles__f_agg_mean__isabs_True__qh_0.8__ql_0.2': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.change_quantiles, f_agg="mean", isabs=True, qh=0.8, ql=0.2)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_fft_0_abs_attr': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.fft_coefficient, [{"attr":"abs", "coeff":0}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_fft_6_abs_attr': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.fft_coefficient, [{"attr":"abs", "coeff":6}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_fft_11_abs_attr': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.fft_coefficient, [{"attr":"abs", "coeff":11}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_fft_0_real_attr': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.fft_coefficient, [{"attr":"real", "coeff":0}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_fft_12_abs_attr': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.fft_coefficient, [{"attr":"abs", "coeff":12}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_fft_1_imag_attr': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.fft_coefficient, [{"attr":"imag", "coeff":1}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_change_quantiles_f_agg_var__isabs_False__qh_1.0__ql_0.8': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.change_quantiles, f_agg="var", isabs=False, qh=1.0, ql=0.8)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_change_quantiles_f_agg_var__isabs_True__qh_0.8__ql_0.6': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.change_quantiles, f_agg="var", isabs=True, qh=0.8, ql=0.6)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_change_quantiles_f_agg_mean__isabs_True__qh_0.8__ql_0.2': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.change_quantiles, f_agg="mean", isabs=True, qh=0.8, ql=0.2)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_change_quantiles_f_agg_var__isabs_True__qh_0.6__ql_0.2': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.change_quantiles, f_agg="var", isabs=True, qh=0.6, ql=0.2)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_maximum': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.maximum)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_approx_entropy_2_0.7': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.approximate_entropy, 2, 0.7)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_approx_entropy_2_0.3': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.approximate_entropy, 2, 0.3)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_approx_entropy_2_0.9': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.approximate_entropy, 2, 0.9)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_longest_strike_below_mean': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.longest_strike_below_mean)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_autocorrelation__lag_1': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.autocorrelation, 1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_agg_linear_trend__f_agg_max__chunk_len_10__attr_stderr': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(np.array), M(fc.agg_linear_trend, [{'attr': 'stderr', 'chunk_len': 10, 'f_agg': 'max'}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_spkt_welch_density__coeff_2': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.spkt_welch_density, [{"coeff":2}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_partial_autocorrelation__lag_1': {
        'inputs': [
            'feat_belt_accel_magnitude'
        ],
        'function': C(slicer('5s'), M(fc.partial_autocorrelation, [{"lag":1}], default=((0, 0))), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_agg_linear_trend__f_agg_mean__chunk_len_50__attr_stderr': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(np.array), M(fc.agg_linear_trend, [{'attr': 'stderr', 'chunk_len': 50, 'f_agg': 'mean'}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_agg_linear_trend__f_agg_max__chunk_len_5__attr_stderr': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(np.array), M(fc.agg_linear_trend, [{'attr': 'stderr', 'chunk_len': 5, 'f_agg': 'max'}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_skewness': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.skewness)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_agg_linear_trend__f_agg_max__chunk_len_50__attr_stderr': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(np.array), M(fc.agg_linear_trend, [{'attr': 'stderr', 'chunk_len': 50, 'f_agg': 'max'}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_number_crossing_m__m_1': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.number_crossing_m, 1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_number_peaks__n_1': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.number_peaks, 1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__c3__lag_2': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.c3, 2)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__quantile__q_0.3': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.quantile, 0.3)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__range_count__max_1__min_-1': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(np.array), M(fc.range_count, -1, 1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__sum_values': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(sum)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__linear_trend__attr_intercept': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.linear_trend, [{"attr":"intercept"}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },


    'feat_belt_accel_magnitude__abs_energy': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.abs_energy)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__quantile__q_0.6': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.quantile, 0.6)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__median': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(np.median)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__quantile__q_0.1': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.quantile, 0.1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__quantile__q_0.2': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.quantile, 0.2)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__quantile__q_0.4': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.quantile, 0.4)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__mean': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(np.mean)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__c3__lag_3': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.c3, 3)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude__c3__lag_1': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(fc.c3, 1)),
        'window': '',
        'default': 0
    },

    'feat_belt_accel_magnitude_agg_linear_trend__f_agg_mean__chunk_len_50__attr_intercept': {
        'inputs': [
            'feat_belt_accel_magnitude',
        ],
        'function': C(slicer('5s'), M(np.array), M(fc.agg_linear_trend, [{'attr': 'intercept', 'chunk_len': 50, 'f_agg': 'mean'}]), extract_component(0), extract_component(1)),
        'window': '',
        'default': 0
    },

    'feat_mobility_activity': {
        'inputs': [
            'feat_belt_accel_magnitude__abs_energy',
            'feat_belt_accel_magnitude__c3__lag_1',
            'feat_belt_accel_magnitude__c3__lag_2',
            'feat_belt_accel_magnitude__c3__lag_3',
            'feat_belt_accel_magnitude__linear_trend__attr_intercept',
            'feat_belt_accel_magnitude__mean',
            'feat_belt_accel_magnitude__median',
            'feat_belt_accel_magnitude__quantile__q_0.1',
            'feat_belt_accel_magnitude__quantile__q_0.2',
            'feat_belt_accel_magnitude__quantile__q_0.3',
            'feat_belt_accel_magnitude__quantile__q_0.4',
            'feat_belt_accel_magnitude__quantile__q_0.6',
            'feat_belt_accel_magnitude__range_count__max_1__min_-1',
            'feat_belt_accel_magnitude__sum_values',
            'feat_belt_accel_magnitude_agg_linear_trend__f_agg_max__chunk_len_10__attr_stderr',
            'feat_belt_accel_magnitude_agg_linear_trend__f_agg_max__chunk_len_50__attr_stderr',
            'feat_belt_accel_magnitude_agg_linear_trend__f_agg_max__chunk_len_5__attr_stderr',
            'feat_belt_accel_magnitude_agg_linear_trend__f_agg_mean__chunk_len_50__attr_intercept',
            'feat_belt_accel_magnitude_agg_linear_trend__f_agg_mean__chunk_len_50__attr_stderr',
            'feat_belt_accel_magnitude_approx_entropy_2_0.3',
            'feat_belt_accel_magnitude_approx_entropy_2_0.5',
            'feat_belt_accel_magnitude_approx_entropy_2_0.7',
            'feat_belt_accel_magnitude_approx_entropy_2_0.9',
            'feat_belt_accel_magnitude_autocorrelation__lag_1',
            'feat_belt_accel_magnitude_change_quantiles__f_agg_mean__isabs_True__qh_0.8__ql_0.2',
            'feat_belt_accel_magnitude_change_quantiles_f_agg_mean__isabs_True__qh_0.8__ql_0.2',
            'feat_belt_accel_magnitude_change_quantiles_f_agg_var__isabs_False__qh_1.0__ql_0.8',
            'feat_belt_accel_magnitude_change_quantiles_f_agg_var__isabs_True__qh_0.6__ql_0.2',
            'feat_belt_accel_magnitude_change_quantiles_f_agg_var__isabs_True__qh_0.8__ql_0.6',
            'feat_belt_accel_magnitude_fft_0_abs_attr',
            'feat_belt_accel_magnitude_fft_0_real_attr',
            'feat_belt_accel_magnitude_fft_11_abs_attr',
            'feat_belt_accel_magnitude_fft_12_abs_attr',
            'feat_belt_accel_magnitude_fft_1_imag_attr',
            'feat_belt_accel_magnitude_fft_6_abs_attr',
            'feat_belt_accel_magnitude_longest_strike_below_mean',
            'feat_belt_accel_magnitude_maximum',
            'feat_belt_accel_magnitude_number_crossing_m__m_1',
            'feat_belt_accel_magnitude_number_peaks__n_1',
            'feat_belt_accel_magnitude_partial_autocorrelation__lag_1',
            'feat_belt_accel_magnitude_skewness',
            'feat_belt_accel_magnitude_spkt_welch_density__coeff_2',
        ],
         'function': run_ml_model('test_clf_walk-still'),
         'window': '',
         'store': True
    },

    'feat_mobility_activity_current': {
        'inputs': [
            'feat_mobility_activity'
        ],
        'window': '',
        'function': alias
    },

    # mobility_stand_up pipeline
    'feat_mobility_stand_up_count': {
        'inputs': [
        ],
        'function': constant('medium'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_stand_up_mode': {
        'inputs': [
        ],
        'function': constant('no_hands'),
        'window': '24h',
        'store': True
    },
    
    'feat_mobility_stand_up_time': {
        'inputs': [
        ],
        'function': constant('fast'),
        'window': '24h',
        'store': True
    },

    'situ_mobility_stand_up_predicted': {
        'inputs': [
        ],
        'function': constant('high'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_stand_up_count_weekly': {
        'inputs': [
        ],
        'function': constant(0),
        'window': '24h',
        'store': True
    },

    # mobility_standing pipeline
    'feat_mobility_standing_episode_length': {
        'inputs': [
        ],
        'function': constant('long'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_standing_mode': {
        'inputs': [
        ],
        'function': constant('no_aids'),
        'window': '24h',
        'store': True
    },
    
    'feat_mobility_standing_daily_duration': {
        'inputs': [
        ],
        'function': constant('high'),
        'window': '24h',
        'store': True
    },

    'situ_mobility_standing_predicted': {
        'inputs': [
        ],
        'function': constant('high'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_standing_duration_weekly': {
        'inputs': [
        ],
        'function': constant(0),
        'window': '24h',
        'store': True
    },

    # mobility_walking pipeline
    'feat_mobility_walking_longest_episode': {
        'inputs': [
            'feat_mobility_activity'
        ],
        'function': longest_walking_episode,
        'window': '24h',
        'store': True
    },

    'feat_mobility_walking_episode_distance_qualitative': {
        'inputs': [
            'feat_mobility_walking_longest_episode'
        ],
        'function': walking_episode_qualitative,
        'window': '24h',
        'default': 'normal_or_high',
        'store': True
    },

    'feat_mobility_walking_daily_distance_qualitative': {
        'inputs': [
            'feat_mobility_walking_duration_qualitative'
        ],
        'function': alias,
        'window': '24h',
        'default': 'medium',
        'store': True
    },

    'feat_mobility_walking_duration': {
        'inputs': [
            'feat_mobility_activity'
        ],
        'function': cumulative_walking_time,
        'window': '24h',
        'store': True
    },

    'feat_mobility_walking_duration_qualitative': {
        'inputs': [
            'feat_mobility_walking_duration'
        ],
        'function': cumulative_walking_time_qualitative,
        'window': '24h',
        'default': 'medium',
        'store': True
    },

    'feat_mobility_walking_mode': {
        'inputs': [
        ],
        'function': constant('mostly_unaided'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_walking_instabilities_count': {
        'inputs': [
        ],
        'function': constant('some'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_walking_falls_count': {
        'inputs': [
        ],
        'function': constant('some'),
        'window': '24h',
        'store': True
    },

    'situ_mobility_walking_predicted': {
        'inputs': [
            ('situ_mobility_walking', '4d')
        ],
        'function': mode,
        'window': '24h',
        'default': 'medium',
        'store': True
    },

    'feat_mobility_walking_step_count_weekly': {
        'inputs': [
        ],
        'function': constant(0),
        'window': '24h',
        'store': True
    },

    'feat_mobility_walking_distance_weekly': {
        'inputs': [
        ],
        'function': constant(0),
        'window': '24h',
        'store': True
    },

    # mobility_use_stairs pipeline
    'feat_mobility_use_stairs_mode': {
        'inputs': [
        ],
        'function': constant('mostly_unaided'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_use_stairs_count': {
        'inputs': [
        ],
        'function': constant('many'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_use_stairs_time_per': {
        'inputs': [
        ],
        'function': constant('short'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_use_stairs_rest_count': {
        'inputs': [
        ],
        'function': constant('few'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_use_stairs_rest_duration': {
        'inputs': [
        ],
        'function': constant('short'),
        'window': '24h',
        'store': True
    },

    'situ_mobility_use_stairs_predicted': {
        'inputs': [
        ],
        'function': constant('high'),
        'window': '24h',
        'store': True
    },

    'feat_mobility_use_stairs_count_weekly': {
        'inputs': [
        ],
        'function': constant(0),
        'window': '24h',
        'store': True
    },

    # mobility_instructed_walking
    'feat_walking_longest_episode_length': {
        'inputs': [
            ('feat_mobility_activity', '24h')
        ],
        'function': C(midnight_filter, longest_walking_episode),
        'window': '4h',
        'default': 0,
        'store': True
    },

    'feat_walking_longest_episode_exceeded': {
        'inputs': [
            'feat_walking_longest_episode_length',
            'feat_mobility_activity_current'
        ],
        'function': longest_walking_episode_vs_prescribed,
        'window': '4h',
        'store': True
    },
    
    'feat_walking_time_cumulative': {
        'inputs': [
            ('feat_mobility_activity', '24h')
        ],
        'function': C(midnight_filter, cumulative_walking_time),
        'window': '4h',
        'default': 0,
        'store': True
    },

    'feat_walking_time_threshold_reached': {
        'inputs': [
            'feat_walking_time_cumulative',
            'feat_mobility_activity_current'
        ],
        'function': cumulative_walking_time_vs_prescribed,
        'window': '4h',
        'store': True
    }
}
