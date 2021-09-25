##################################################################################
##########--this is an autogenerated python model definition for proDEX--#########
##--original file: Total_Assessment_v05_forprodex.dxi --##
##################################################################################

from .lib.proDEX import *

situ_social_activity_general = Node()
Relative_activity_Total = Node()
calls_last_7_days = Node()
visits_last_7_days = Node()
together_outside_last_7_days = Node()
Absolute_daily_activity_Total = Node()
feat_calls_count_total_relative = Atrib()
feat_calls_duration_total_relative = Atrib()
feat_visits_total_relative_past_week = Atrib()
feat_visits_total_relative = Atrib()
feat_outside_total_relative_past_week = Atrib()
feat_outside_total_relative = Atrib()
feat_calls_count_total_weekly_vs_goal = Atrib()
feat_visits_count_total_weekly_vs_goal = Atrib()
feat_outside_count_total_weekly_vs_goal = Atrib()

situ_social_activity_general.setName('situ_social_activity_general')
Relative_activity_Total.setName('Relative_activity_Total')
calls_last_7_days.setName('calls_last_7_days')
visits_last_7_days.setName('visits_last_7_days')
together_outside_last_7_days.setName('together_outside_last_7_days')
Absolute_daily_activity_Total.setName('Absolute_daily_activity_Total')
feat_calls_count_total_relative.setName('feat_calls_count_total_relative')
feat_calls_duration_total_relative.setName('feat_calls_duration_total_relative')
feat_visits_total_relative_past_week.setName('feat_visits_total_relative_past_week')
feat_visits_total_relative.setName('feat_visits_total_relative')
feat_outside_total_relative_past_week.setName('feat_outside_total_relative_past_week')
feat_outside_total_relative.setName('feat_outside_total_relative')
feat_calls_count_total_weekly_vs_goal.setName('feat_calls_count_total_weekly_vs_goal')
feat_visits_count_total_weekly_vs_goal.setName('feat_visits_count_total_weekly_vs_goal')
feat_outside_count_total_weekly_vs_goal.setName('feat_outside_count_total_weekly_vs_goal')

situ_social_activity_general.setValues(['very_low', 'low', 'medium', 'high', 'very_high'])
Relative_activity_Total.setValues(['high decrease', 'decrease', 'stable', 'increase', 'high increase'])
calls_last_7_days.setValues(['decrease', 'stable', 'increase'])
visits_last_7_days.setValues(['decrease', 'stable', 'increase'])
together_outside_last_7_days.setValues(['decrease', 'stable', 'increase'])
Absolute_daily_activity_Total.setValues(['very low', 'low', 'medium', 'high', 'very high'])
feat_calls_count_total_relative.setValues(['decrease', 'stable', 'increase'])
feat_calls_duration_total_relative.setValues(['decrease', 'stable', 'increase'])
feat_visits_total_relative_past_week.setValues(['decrease', 'stable', 'increase'])
feat_visits_total_relative.setValues(['decrease', 'stable', 'increase'])
feat_outside_total_relative_past_week.setValues(['decrease', 'stable', 'increase'])
feat_outside_total_relative.setValues(['decrease', 'stable', 'increase'])
feat_calls_count_total_weekly_vs_goal.setValues(['low', 'medium', 'high'])
feat_visits_count_total_weekly_vs_goal.setValues(['low', 'medium', 'high'])
feat_outside_count_total_weekly_vs_goal.setValues(['low', 'medium', 'high'])

situ_social_activity_general.addChild(Relative_activity_Total)
Relative_activity_Total.setParent(situ_social_activity_general)
situ_social_activity_general.addChild(Absolute_daily_activity_Total)
Absolute_daily_activity_Total.setParent(situ_social_activity_general)
Relative_activity_Total.addChild(calls_last_7_days)
calls_last_7_days.setParent(Relative_activity_Total)
Relative_activity_Total.addChild(visits_last_7_days)
visits_last_7_days.setParent(Relative_activity_Total)
Relative_activity_Total.addChild(together_outside_last_7_days)
together_outside_last_7_days.setParent(Relative_activity_Total)
calls_last_7_days.addChild(feat_calls_count_total_relative)
feat_calls_count_total_relative.setParent(calls_last_7_days)
calls_last_7_days.addChild(feat_calls_duration_total_relative)
feat_calls_duration_total_relative.setParent(calls_last_7_days)
visits_last_7_days.addChild(feat_visits_total_relative_past_week)
feat_visits_total_relative_past_week.setParent(visits_last_7_days)
visits_last_7_days.addChild(feat_visits_total_relative)
feat_visits_total_relative.setParent(visits_last_7_days)
together_outside_last_7_days.addChild(feat_outside_total_relative_past_week)
feat_outside_total_relative_past_week.setParent(together_outside_last_7_days)
together_outside_last_7_days.addChild(feat_outside_total_relative)
feat_outside_total_relative.setParent(together_outside_last_7_days)
Absolute_daily_activity_Total.addChild(feat_calls_count_total_weekly_vs_goal)
feat_calls_count_total_weekly_vs_goal.setParent(Absolute_daily_activity_Total)
Absolute_daily_activity_Total.addChild(feat_visits_count_total_weekly_vs_goal)
feat_visits_count_total_weekly_vs_goal.setParent(Absolute_daily_activity_Total)
Absolute_daily_activity_Total.addChild(feat_outside_count_total_weekly_vs_goal)
feat_outside_count_total_weekly_vs_goal.setParent(Absolute_daily_activity_Total)

situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high decrease', Absolute_daily_activity_Total:'very low'}, 'very_low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high decrease', Absolute_daily_activity_Total:'low'}, 'very_low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high decrease', Absolute_daily_activity_Total:'medium'}, 'low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high decrease', Absolute_daily_activity_Total:'high'}, 'medium'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high decrease', Absolute_daily_activity_Total:'very high'}, 'high'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'decrease', Absolute_daily_activity_Total:'very low'}, 'very_low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'decrease', Absolute_daily_activity_Total:'low'}, 'low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'decrease', Absolute_daily_activity_Total:'medium'}, 'medium'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'decrease', Absolute_daily_activity_Total:'high'}, 'high'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'decrease', Absolute_daily_activity_Total:'very high'}, 'very_high'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'stable', Absolute_daily_activity_Total:'very low'}, 'very_low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'stable', Absolute_daily_activity_Total:'low'}, 'low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'stable', Absolute_daily_activity_Total:'medium'}, 'medium'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'stable', Absolute_daily_activity_Total:'high'}, 'high'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'stable', Absolute_daily_activity_Total:'very high'}, 'very_high'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'increase', Absolute_daily_activity_Total:'very low'}, 'very_low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'increase', Absolute_daily_activity_Total:'low'}, 'low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'increase', Absolute_daily_activity_Total:'medium'}, 'medium'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'increase', Absolute_daily_activity_Total:'high'}, 'high'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'increase', Absolute_daily_activity_Total:'very high'}, 'very_high'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high increase', Absolute_daily_activity_Total:'very low'}, 'low'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high increase', Absolute_daily_activity_Total:'low'}, 'medium'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high increase', Absolute_daily_activity_Total:'medium'}, 'high'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high increase', Absolute_daily_activity_Total:'high'}, 'very_high'])
situ_social_activity_general.addFunctionRow([{Relative_activity_Total:'high increase', Absolute_daily_activity_Total:'very high'}, 'very_high'])

Relative_activity_Total.addFunctionRow([{calls_last_7_days:'decrease', visits_last_7_days:'decrease', together_outside_last_7_days:'decrease'}, 'high decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'decrease', visits_last_7_days:'decrease', together_outside_last_7_days:'stable'}, 'high decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'decrease', visits_last_7_days:'decrease', together_outside_last_7_days:'increase'}, 'decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'decrease', visits_last_7_days:'stable', together_outside_last_7_days:'decrease'}, 'high decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'decrease', visits_last_7_days:'stable', together_outside_last_7_days:'stable'}, 'decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'decrease', visits_last_7_days:'stable', together_outside_last_7_days:'increase'}, 'stable'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'decrease', visits_last_7_days:'increase', together_outside_last_7_days:'decrease'}, 'decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'decrease', visits_last_7_days:'increase', together_outside_last_7_days:'stable'}, 'stable'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'decrease', visits_last_7_days:'increase', together_outside_last_7_days:'increase'}, 'increase'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'stable', visits_last_7_days:'decrease', together_outside_last_7_days:'decrease'}, 'high decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'stable', visits_last_7_days:'decrease', together_outside_last_7_days:'stable'}, 'decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'stable', visits_last_7_days:'decrease', together_outside_last_7_days:'increase'}, 'stable'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'stable', visits_last_7_days:'stable', together_outside_last_7_days:'decrease'}, 'decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'stable', visits_last_7_days:'stable', together_outside_last_7_days:'stable'}, 'stable'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'stable', visits_last_7_days:'stable', together_outside_last_7_days:'increase'}, 'increase'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'stable', visits_last_7_days:'increase', together_outside_last_7_days:'decrease'}, 'stable'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'stable', visits_last_7_days:'increase', together_outside_last_7_days:'stable'}, 'increase'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'stable', visits_last_7_days:'increase', together_outside_last_7_days:'increase'}, 'high increase'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'increase', visits_last_7_days:'decrease', together_outside_last_7_days:'decrease'}, 'decrease'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'increase', visits_last_7_days:'decrease', together_outside_last_7_days:'stable'}, 'stable'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'increase', visits_last_7_days:'decrease', together_outside_last_7_days:'increase'}, 'increase'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'increase', visits_last_7_days:'stable', together_outside_last_7_days:'decrease'}, 'stable'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'increase', visits_last_7_days:'stable', together_outside_last_7_days:'stable'}, 'increase'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'increase', visits_last_7_days:'stable', together_outside_last_7_days:'increase'}, 'high increase'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'increase', visits_last_7_days:'increase', together_outside_last_7_days:'decrease'}, 'increase'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'increase', visits_last_7_days:'increase', together_outside_last_7_days:'stable'}, 'high increase'])
Relative_activity_Total.addFunctionRow([{calls_last_7_days:'increase', visits_last_7_days:'increase', together_outside_last_7_days:'increase'}, 'high increase'])

calls_last_7_days.addFunctionRow([{feat_calls_count_total_relative:'decrease', feat_calls_duration_total_relative:'decrease'}, 'decrease'])
calls_last_7_days.addFunctionRow([{feat_calls_count_total_relative:'decrease', feat_calls_duration_total_relative:'stable'}, 'decrease'])
calls_last_7_days.addFunctionRow([{feat_calls_count_total_relative:'decrease', feat_calls_duration_total_relative:'increase'}, 'stable'])
calls_last_7_days.addFunctionRow([{feat_calls_count_total_relative:'stable', feat_calls_duration_total_relative:'decrease'}, 'decrease'])
calls_last_7_days.addFunctionRow([{feat_calls_count_total_relative:'stable', feat_calls_duration_total_relative:'stable'}, 'stable'])
calls_last_7_days.addFunctionRow([{feat_calls_count_total_relative:'stable', feat_calls_duration_total_relative:'increase'}, 'increase'])
calls_last_7_days.addFunctionRow([{feat_calls_count_total_relative:'increase', feat_calls_duration_total_relative:'decrease'}, 'stable'])
calls_last_7_days.addFunctionRow([{feat_calls_count_total_relative:'increase', feat_calls_duration_total_relative:'stable'}, 'increase'])
calls_last_7_days.addFunctionRow([{feat_calls_count_total_relative:'increase', feat_calls_duration_total_relative:'increase'}, 'increase'])

visits_last_7_days.addFunctionRow([{feat_visits_total_relative_past_week:'decrease', feat_visits_total_relative:'decrease'}, 'decrease'])
visits_last_7_days.addFunctionRow([{feat_visits_total_relative_past_week:'decrease', feat_visits_total_relative:'stable'}, 'stable'])
visits_last_7_days.addFunctionRow([{feat_visits_total_relative_past_week:'decrease', feat_visits_total_relative:'increase'}, 'increase'])
visits_last_7_days.addFunctionRow([{feat_visits_total_relative_past_week:'stable', feat_visits_total_relative:'decrease'}, 'decrease'])
visits_last_7_days.addFunctionRow([{feat_visits_total_relative_past_week:'stable', feat_visits_total_relative:'stable'}, 'stable'])
visits_last_7_days.addFunctionRow([{feat_visits_total_relative_past_week:'stable', feat_visits_total_relative:'increase'}, 'increase'])
visits_last_7_days.addFunctionRow([{feat_visits_total_relative_past_week:'increase', feat_visits_total_relative:'decrease'}, 'decrease'])
visits_last_7_days.addFunctionRow([{feat_visits_total_relative_past_week:'increase', feat_visits_total_relative:'stable'}, 'stable'])
visits_last_7_days.addFunctionRow([{feat_visits_total_relative_past_week:'increase', feat_visits_total_relative:'increase'}, 'increase'])

together_outside_last_7_days.addFunctionRow([{feat_outside_total_relative_past_week:'decrease', feat_outside_total_relative:'decrease'}, 'decrease'])
together_outside_last_7_days.addFunctionRow([{feat_outside_total_relative_past_week:'decrease', feat_outside_total_relative:'stable'}, 'decrease'])
together_outside_last_7_days.addFunctionRow([{feat_outside_total_relative_past_week:'decrease', feat_outside_total_relative:'increase'}, 'stable'])
together_outside_last_7_days.addFunctionRow([{feat_outside_total_relative_past_week:'stable', feat_outside_total_relative:'decrease'}, 'decrease'])
together_outside_last_7_days.addFunctionRow([{feat_outside_total_relative_past_week:'stable', feat_outside_total_relative:'stable'}, 'stable'])
together_outside_last_7_days.addFunctionRow([{feat_outside_total_relative_past_week:'stable', feat_outside_total_relative:'increase'}, 'increase'])
together_outside_last_7_days.addFunctionRow([{feat_outside_total_relative_past_week:'increase', feat_outside_total_relative:'decrease'}, 'decrease'])
together_outside_last_7_days.addFunctionRow([{feat_outside_total_relative_past_week:'increase', feat_outside_total_relative:'stable'}, 'stable'])
together_outside_last_7_days.addFunctionRow([{feat_outside_total_relative_past_week:'increase', feat_outside_total_relative:'increase'}, 'increase'])

Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'low', feat_visits_count_total_weekly_vs_goal:'low', feat_outside_count_total_weekly_vs_goal:'low'}, 'very low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'low', feat_visits_count_total_weekly_vs_goal:'low', feat_outside_count_total_weekly_vs_goal:'medium'}, 'very low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'low', feat_visits_count_total_weekly_vs_goal:'low', feat_outside_count_total_weekly_vs_goal:'high'}, 'low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'low', feat_visits_count_total_weekly_vs_goal:'medium', feat_outside_count_total_weekly_vs_goal:'low'}, 'very low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'low', feat_visits_count_total_weekly_vs_goal:'medium', feat_outside_count_total_weekly_vs_goal:'medium'}, 'low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'low', feat_visits_count_total_weekly_vs_goal:'medium', feat_outside_count_total_weekly_vs_goal:'high'}, 'medium'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'low', feat_visits_count_total_weekly_vs_goal:'high', feat_outside_count_total_weekly_vs_goal:'low'}, 'low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'low', feat_visits_count_total_weekly_vs_goal:'high', feat_outside_count_total_weekly_vs_goal:'medium'}, 'medium'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'low', feat_visits_count_total_weekly_vs_goal:'high', feat_outside_count_total_weekly_vs_goal:'high'}, 'high'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'medium', feat_visits_count_total_weekly_vs_goal:'low', feat_outside_count_total_weekly_vs_goal:'low'}, 'very low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'medium', feat_visits_count_total_weekly_vs_goal:'low', feat_outside_count_total_weekly_vs_goal:'medium'}, 'low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'medium', feat_visits_count_total_weekly_vs_goal:'low', feat_outside_count_total_weekly_vs_goal:'high'}, 'medium'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'medium', feat_visits_count_total_weekly_vs_goal:'medium', feat_outside_count_total_weekly_vs_goal:'low'}, 'low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'medium', feat_visits_count_total_weekly_vs_goal:'medium', feat_outside_count_total_weekly_vs_goal:'medium'}, 'medium'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'medium', feat_visits_count_total_weekly_vs_goal:'medium', feat_outside_count_total_weekly_vs_goal:'high'}, 'high'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'medium', feat_visits_count_total_weekly_vs_goal:'high', feat_outside_count_total_weekly_vs_goal:'low'}, 'medium'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'medium', feat_visits_count_total_weekly_vs_goal:'high', feat_outside_count_total_weekly_vs_goal:'medium'}, 'high'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'medium', feat_visits_count_total_weekly_vs_goal:'high', feat_outside_count_total_weekly_vs_goal:'high'}, 'very high'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'high', feat_visits_count_total_weekly_vs_goal:'low', feat_outside_count_total_weekly_vs_goal:'low'}, 'low'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'high', feat_visits_count_total_weekly_vs_goal:'low', feat_outside_count_total_weekly_vs_goal:'medium'}, 'medium'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'high', feat_visits_count_total_weekly_vs_goal:'low', feat_outside_count_total_weekly_vs_goal:'high'}, 'high'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'high', feat_visits_count_total_weekly_vs_goal:'medium', feat_outside_count_total_weekly_vs_goal:'low'}, 'medium'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'high', feat_visits_count_total_weekly_vs_goal:'medium', feat_outside_count_total_weekly_vs_goal:'medium'}, 'high'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'high', feat_visits_count_total_weekly_vs_goal:'medium', feat_outside_count_total_weekly_vs_goal:'high'}, 'very high'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'high', feat_visits_count_total_weekly_vs_goal:'high', feat_outside_count_total_weekly_vs_goal:'low'}, 'high'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'high', feat_visits_count_total_weekly_vs_goal:'high', feat_outside_count_total_weekly_vs_goal:'medium'}, 'very high'])
Absolute_daily_activity_Total.addFunctionRow([{feat_calls_count_total_weekly_vs_goal:'high', feat_visits_count_total_weekly_vs_goal:'high', feat_outside_count_total_weekly_vs_goal:'high'}, 'very high'])

