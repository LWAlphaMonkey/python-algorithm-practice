"""
Repeatedly steps through the list to be sorted, compares each pair of adjacent items
and swaps them if they are in the wrong order.
"""

from __future__ import print_function

def bubble_sort(array):
    """ Return array, sorted with bubble sort """
    arr_len = len(array)
    idx_i = 0
    while idx_i < arr_len:
        idx_j = 1
        while idx_j < (arr_len - idx_i):
            if array[idx_j - 1] > array[idx_j]:
                # swap array[idx_j - 1], array[idx_j]
                tmp = array[idx_j - 1]
                array[idx_j - 1] = array[idx_j]
                array[idx_j] = tmp
            idx_j += 1
        idx_i += 1

    return array

# other version
# def bubbleSort(nlist):
#     for passnum in range(len(nlist) - 1, 0, -1):
#         for i in range(passnum):
#             if nlist[i] > nlist[i + 1]:
#                 temp = nlist[i]
#                 nlist[i] = nlist[i + 1]
#                 nlist[i + 1] = temp

print(bubble_sort([5, 3, 8, 2, 1, 4]))
print(bubble_sort([5, 3, 9, 6, 1, 7, 4, 5]))
