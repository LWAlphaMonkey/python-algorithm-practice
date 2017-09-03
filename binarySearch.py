""" Search for a given value (key) inside of a list (numArray)"""
""" Runs in O(log n) run time - very performant"""
""" Can be written as a recursive function"""
""" numArray must be sorted"""
def binarySearch(numArray, key):
    middleIdx = len(numArray) // 2
    middleElem = numArray[middleIdx]

    if key == middleElem:
        return True
    elif key > middleElem and len(numArray) > 1:
        return binarySearch(numArray[middleIdx:len(numArray)], key)
    elif key < middleElem and len(numArray) > 1:
        return binarySearch(numArray[:middleIdx], key)
    else:
        return False

print(binarySearch([5, 7, 12, 16, 36, 39, 42, 56, 71], 56))
print(binarySearch([5, 7, 12, 16, 36, 39, 42, 56, 71], 72))
