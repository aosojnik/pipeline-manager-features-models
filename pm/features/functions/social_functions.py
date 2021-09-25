from ...utils import profile_lookup

def relative_qualitative(timestamp, timestep, inputs):
    weekly = None
    total = None
    for inpt in inputs:
        if "_weekly" in inpt:
            weekly = inputs[inpt][0][2]
        elif "_total" in inpt or "_past_week" in inpt:
            t = inputs[inpt]
            total = t[0][2] if t else 0
    
    val = "stable"
    if total == 0:
        pass
    elif weekly / total <= 0.90:
        val = "decrease"
    elif weekly / total <= 1.10:
        val = "increase"

    return [(timestamp, timestep, val)]

def versus_goal(goal_name):
    def vs(timestamp, timestep, inputs):
        goal = profile_lookup(goal_name)
        r = next(iter(inputs.values()))
        reached = r[0][2] if r else 0

        val = None
        if goal == 0:
            val = "high"
        elif reached / goal < 0.5:
            val = "low"
        elif reached / goal < 1:
            val = "medium"
        else:
            val = "high"
        
        return [(timestamp, timestep, val)]
    return vs


def lowest_activity(timestamp, timestep, inputs):
    calls_key = [k for k in inputs.keys() if 'calls' in k][0]
    visits_key = [k for k in inputs.keys() if 'visits' in k][0]
    outside_key = [k for k in inputs.keys() if 'outside' in k][0]
    calls = inputs[calls_key][0][2]
    visits = inputs[visits_key][0][2]
    outside = inputs[outside_key][0][2]

    low = ({'calls'} if calls == 'low' else set()) | ({'visits'} if visits == 'low' else set()) | ({'together_outside'} if outside == 'low' else set())
    medium = ({'calls'} if calls == 'medium' else set()) | ({'visits'} if visits == 'medium' else set()) | ({'together_outside'} if outside == 'medium' else set())
    high = ({'calls'} if calls == 'high' else set()) | ({'visits'} if visits == 'high' else set()) | ({'together_outside'} if outside == 'high' else set())

    val = 'none'
    if low:
        val = next(iter(low))
    elif medium:
        val = next(iter(medium))

    return [(timestamp, timestep, val)]

def interaction_preferrence(timestamp, timestep, inputs):
    to_pu = profile_lookup("renderingToMe")
    to_su = profile_lookup("renderingToCoach")

    if to_pu and not to_su:
        val = "to_PU"
    elif to_su and not to_pu:
        val = "to_SU"
    else:
        val = "no_preference"
    
    return [(timestamp, timestep, val)]

def invite_possible(timestamp, timestep, inputs):
    contacts = profile_lookup('contacts')
    return [(timestamp, timestep, "yes" if any(p['canInvite'] for p in contacts) else "no")]

def invite_possible_friends(timestamp, timestep, inputs):
    contacts = profile_lookup('contacts')
    return [(timestamp, timestep, "yes" if any(p['canInvite'] for p in contacts if p['type'] == "Friends") else "no")]

def invite_possible_family(timestamp, timestep, inputs):
    contacts = profile_lookup('contacts')
    return [(timestamp, timestep, "yes" if any(p['canInvite'] for p in contacts if p['type'] == "Family") else "no")]

def event_available(timestamp, timestep, inputs):
    events = profile_lookup('events')
    return [(timestamp, timestep, "yes" if len(events) else "no")]

def nonhabitual_presence(timestamp, timestep, inputs):
    return [(timestamp, timestep, 'at_some')]