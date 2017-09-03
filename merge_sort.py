"""Conceptually, a merge sort works as follows:

   Divide the unsorted list into n sublists, each containing 1 element
   (a list of 1 element is considered sorted).

   Repeatedly merge sublists to produce new sorted sublists until there is
   only 1 sublist remaining. This will be the sorted.
"""

from __future__ import print_function

def merge_sort(array):
    """
    Take in a single, unsorted array as a parameter
    split the array into two halves
    """
    if len(array) < 2:
        return array

    middle_idx = len(array) // 2
    first_half = list(array[0:middle_idx])
    second_half = list(array[middle_idx:])

    return merge(merge_sort(first_half), merge_sort(second_half))

def merge(array_1, array_2):
    """
    Take in two sorted arrays as parameters
    merge those sorted arrays into one sorted array
    return one sorted array
    """
    result = []

    while array_1 and array_2:
        if array_1[0] < array_2[0]:
            min_elem = array_1.pop(0)
            result.append(min_elem)
        elif array_1[0] > array_2[0]:
            min_elem = array_2.pop(0)
            result.append(min_elem)
        elif array_1[0] == array_2[0]:
            result.append(array_1.pop(0))
            result.append(array_2.pop(0))

    if array_1:
        result.extend(array_1)
    elif array_2:
        result.extend(array_2)

    return result

print(merge_sort([4, 3, 2, 1]))
print(merge_sort([3, 5, 1, 200, 4, 231, 3523, 1, 45, 97]))
print(merge_sort([100, -20, 40, -30, 16, -100, -101]))
