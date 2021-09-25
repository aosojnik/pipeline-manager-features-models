##################################################################################
##########--this is an autogenerated python model definition for proDEX--#########
##--original file: coach_mobility_instructed_walking.dxi --##
##################################################################################

from .lib.proDEX import *

coach_mobility_instructed_walking = Node()
situ_mobility_instructed_walking = Atrib()

coach_mobility_instructed_walking.setName('coach_mobility_instructed_walking')
situ_mobility_instructed_walking.setName('situ_mobility_instructed_walking')

coach_mobility_instructed_walking.setValues(['no_action', 'warn_of_too_long_episode', 'warn_of_too_long_cumulative', 'warn_of_too_long_episode_and_cumulative'])
situ_mobility_instructed_walking.setValues(['as_instructed', 'too_long_episode', 'too_long_cumulative', 'too_long_episode_and_cumulative'])

coach_mobility_instructed_walking.addChild(situ_mobility_instructed_walking)
situ_mobility_instructed_walking.setParent(coach_mobility_instructed_walking)

coach_mobility_instructed_walking.addFunctionRow([{situ_mobility_instructed_walking:'as_instructed'}, 'no_action'])
coach_mobility_instructed_walking.addFunctionRow([{situ_mobility_instructed_walking:'too_long_episode'}, 'warn_of_too_long_episode'])
coach_mobility_instructed_walking.addFunctionRow([{situ_mobility_instructed_walking:'too_long_cumulative'}, 'warn_of_too_long_cumulative'])
coach_mobility_instructed_walking.addFunctionRow([{situ_mobility_instructed_walking:'too_long_episode_and_cumulative'}, 'warn_of_too_long_episode_and_cumulative'])

