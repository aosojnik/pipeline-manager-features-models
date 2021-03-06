##################################################################################
##########--this is an autogenerated python model definition for proDEX--#########
##--original file: coach_mobility_standing_v04_forprodex.dxi --##
##################################################################################

from .lib.proDEX import *

coach_mobility_standing = Node()
Relative_change = Node()
situ_mobility_standing = Atrib()
situ_mobility_standing_predicted = Atrib()

coach_mobility_standing.setName('coach_mobility_standing')
Relative_change.setName('Relative_change')
situ_mobility_standing.setName('situ_mobility_standing')
situ_mobility_standing_predicted.setName('situ_mobility_standing_predicted')

coach_mobility_standing.setValues(['negative_message_to_PU_or_SU', 'positive_message_to_PU_or_SU', 'no_action'])
Relative_change.setValues(['big_drop', 'medium_drop', 'small_drop', 'no_change', 'small_improvement', 'medium_improvement', 'big_improvement'])
situ_mobility_standing.setValues(['very_low', 'low', 'medium', 'high', 'very_high'])
situ_mobility_standing_predicted.setValues(['very_low', 'low', 'medium', 'high', 'very_high'])

coach_mobility_standing.addChild(situ_mobility_standing)
situ_mobility_standing.setParent(coach_mobility_standing)
coach_mobility_standing.addChild(Relative_change)
Relative_change.setParent(coach_mobility_standing)
Relative_change.addChild(situ_mobility_standing)
situ_mobility_standing.setParent(Relative_change)
Relative_change.addChild(situ_mobility_standing_predicted)
situ_mobility_standing_predicted.setParent(Relative_change)

coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_low', Relative_change:'big_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_low', Relative_change:'medium_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_low', Relative_change:'small_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_low', Relative_change:'no_change'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_low', Relative_change:'small_improvement'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_low', Relative_change:'medium_improvement'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_low', Relative_change:'big_improvement'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'low', Relative_change:'big_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'low', Relative_change:'medium_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'low', Relative_change:'small_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'low', Relative_change:'no_change'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'low', Relative_change:'small_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'low', Relative_change:'medium_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'low', Relative_change:'big_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'medium', Relative_change:'big_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'medium', Relative_change:'medium_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'medium', Relative_change:'small_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'medium', Relative_change:'no_change'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'medium', Relative_change:'small_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'medium', Relative_change:'medium_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'medium', Relative_change:'big_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'high', Relative_change:'big_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'high', Relative_change:'medium_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'high', Relative_change:'small_drop'}, 'negative_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'high', Relative_change:'no_change'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'high', Relative_change:'small_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'high', Relative_change:'medium_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'high', Relative_change:'big_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_high', Relative_change:'big_drop'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_high', Relative_change:'medium_drop'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_high', Relative_change:'small_drop'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_high', Relative_change:'no_change'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_high', Relative_change:'small_improvement'}, 'no_action'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_high', Relative_change:'medium_improvement'}, 'positive_message_to_PU_or_SU'])
coach_mobility_standing.addFunctionRow([{situ_mobility_standing:'very_high', Relative_change:'big_improvement'}, 'positive_message_to_PU_or_SU'])

Relative_change.addFunctionRow([{situ_mobility_standing:'very_low', situ_mobility_standing_predicted:'very_low'}, 'no_change'])
Relative_change.addFunctionRow([{situ_mobility_standing:'very_low', situ_mobility_standing_predicted:'low'}, 'small_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'very_low', situ_mobility_standing_predicted:'medium'}, 'big_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'very_low', situ_mobility_standing_predicted:'high'}, 'big_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'very_low', situ_mobility_standing_predicted:'very_high'}, 'big_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'low', situ_mobility_standing_predicted:'very_low'}, 'small_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'low', situ_mobility_standing_predicted:'low'}, 'no_change'])
Relative_change.addFunctionRow([{situ_mobility_standing:'low', situ_mobility_standing_predicted:'medium'}, 'small_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'low', situ_mobility_standing_predicted:'high'}, 'big_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'low', situ_mobility_standing_predicted:'very_high'}, 'big_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'medium', situ_mobility_standing_predicted:'very_low'}, 'big_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'medium', situ_mobility_standing_predicted:'low'}, 'small_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'medium', situ_mobility_standing_predicted:'medium'}, 'no_change'])
Relative_change.addFunctionRow([{situ_mobility_standing:'medium', situ_mobility_standing_predicted:'high'}, 'small_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'medium', situ_mobility_standing_predicted:'very_high'}, 'big_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'high', situ_mobility_standing_predicted:'very_low'}, 'big_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'high', situ_mobility_standing_predicted:'low'}, 'big_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'high', situ_mobility_standing_predicted:'medium'}, 'small_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'high', situ_mobility_standing_predicted:'high'}, 'no_change'])
Relative_change.addFunctionRow([{situ_mobility_standing:'high', situ_mobility_standing_predicted:'very_high'}, 'small_drop'])
Relative_change.addFunctionRow([{situ_mobility_standing:'very_high', situ_mobility_standing_predicted:'very_low'}, 'big_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'very_high', situ_mobility_standing_predicted:'low'}, 'big_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'very_high', situ_mobility_standing_predicted:'medium'}, 'small_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'very_high', situ_mobility_standing_predicted:'high'}, 'small_improvement'])
Relative_change.addFunctionRow([{situ_mobility_standing:'very_high', situ_mobility_standing_predicted:'very_high'}, 'no_change'])

