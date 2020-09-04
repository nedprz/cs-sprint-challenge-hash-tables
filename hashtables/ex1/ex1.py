def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weights_idx = {}

    for w in range(length):
        weights_idx[weights[w]] = w

    for w in range(length):
        diff = limit - weights[w]

        if diff in weights_idx:
            if weights_idx[diff] > w:
                return (weights_idx[diff],w)
            else:
                return (w,weights_idx[diff])


    return None
