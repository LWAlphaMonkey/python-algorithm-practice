import time
""" memorized fibonacci realization

1. Check to see if number already exists in cache
2. If number is in cache, use that number
3. If number is not in cache, calculate it and put it in cache,
   so it can be used multiple times in future
"""
def fibMemo(index, cache = {}):
    """ realized a memorized fibonacci

    Keyword argument:
    index -- index of number in fibonacci sequence
    cache -- an array used as memory
    """
    if index in cache:
        return cache[index]
    else:
        if index < 3:
            return 1
        else:
            a = fibMemo(index - 1, cache)
            b = fibMemo(index - 2, cache)
            cache[index] = fibMemo(index - 1, cache) + fibMemo(index - 2, cache)

    return cache[index]

for i in range(1, 21):
    t0 = time.time()
    print(fibMemo(i))
    t1 = time.time()
    print("total time: ", t1 - t0)

