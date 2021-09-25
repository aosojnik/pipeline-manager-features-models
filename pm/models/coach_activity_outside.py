

from .lib.proDEX import *

coach_activity_outside = Node()
situ_activity_outside = Atrib()

coach_activity_outside.setName('coach_activity_outside')
situ_activity_outside.setName('situ_activity_outside')

coach_activity_outside.setValues(['positive_message_to_PU_or_SU', 'negative_message_to_PU_or_SU', 'no_action'])
situ_activity_outside.setValues(['less_outside', 'usual_outside', 'more_outside'])

coach_activity_outside.addChild(situ_activity_outside)
situ_activity_outside.setParent(coach_activity_outside)

coach_activity_outside.addFunctionRow([{situ_activity_outside:'less_outside'}, 'negative_message_to_PU_or_SU'])
coach_activity_outside.addFunctionRow([{situ_activity_outside:'usual_outside'}, 'no_action'])
coach_activity_outside.addFunctionRow([{situ_activity_outside:'more_outside'}, 'positive_message_to_PU_or_SU'])

