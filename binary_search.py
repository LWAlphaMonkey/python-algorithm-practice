""" Search for a given value (key) inside of a list (num_array)

    Runs in O(log n) run time - very performant
    Can be written as a recursive function
    P.S. num_array must be sorted
"""

from __future__ import print_function

def binary_search(num_array, key):
    """Return True if the key is in the num_array"""

    middle_idx = len(num_array) // 2
    middle_elem = num_array[middle_idx]

    if key == middle_elem:
        return True
    elif key > middle_elem and len(num_array) > 1:
        return binary_search(num_array[middle_idx:len(num_array)], key)
    elif key < middle_elem and len(num_array) > 1:
        return binary_search(num_array[:middle_idx], key)

    return False

print(binary_search([5, 7, 12, 16, 36, 39, 42, 56, 71], 56))
print(binary_search([5, 7, 12, 16, 36, 39, 42, 56, 71], 72))
