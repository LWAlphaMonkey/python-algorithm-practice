"""Every word should be reversed BUT the string as a whole should not be reversed"""
def reverse(word):
    return word[::-1]

def reverseWords(str):
    eachWords = str.split()
    reversedStr = ''
    for word in eachWords:
        reversedStr += reverse(word) + ' '
    return reversedStr

print(reverseWords('this is a string of words'))
