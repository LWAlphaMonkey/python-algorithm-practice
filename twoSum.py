from __future__ import print_function
"""Returns every pair of numbers from 'numArray' that adds up to the 'sum'"""
def twoSum(num_array, wanted_num):
    """ 1. result should be an array of arrays
        2. any number in the 'numArray' can be used in multiple pairs
        e.g.
        num_array = [1, 6, 4, 5, 3, 3]
        wanted_num = 7
        result = [[6, 1], [3, 4], [3, 4]]"""
    # can be done in O(n^2) time complexity
    # can be done in O(n) time complexity
    hashtable = []
    pairs = []
    for num in num_array:
        counterpart = wanted_num - num

        if counterpart in hashtable:
            pairs.append([num, counterpart])

        hashtable.append(num)

    return pairs

print(twoSum([1, 6, 4, 5, 3, 3], 7))
print(twoSum([40, 11, 19, 17, -12], 28))
