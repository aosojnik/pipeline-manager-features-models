def model_type(root):
    if isinstance(root.tableFunction[0][1], str):
        return 'crisp'
    else:
        return 'probabilistic'

def probabilify(value, node):
    return {v: 1.0 if v == value else 0.0 for v in node.values}

def sample_from_distribution(dist):
    """dist is a dictionary of keys and their probabilities. Output is a single key sampled at random according to the distribution of probabilities."""
    import numpy
    vals = []
    probs = []
    for k in dist:
        if dist[k] is not None:
            vals.append(k)
            probs.append(dist[k])
    probs = [v / sum(probs) for v in probs]
    result = numpy.random.choice(vals, p=probs)
    
    if result == 'toSU_Suggest_to_suggest_action_to_a_third_part':
        # BRUH, OGABNO
        result = 'toSU_Suggest_PU_to_go_out_to_a_social_place_with_someone'
    
    return result