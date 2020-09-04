def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for i in a:
        if -i in cache:                                   # if num has an opposite number of itself in cache
            if i < 0:
                result.append(-i)                        # if num is negative, append the positive version
            else:
                result.append(i)
        else:                                              # if there is not an opposite number, cache the current number
            cache[i] = i                
    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
