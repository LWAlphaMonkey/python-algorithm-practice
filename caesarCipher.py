import string

def caesarCipher(str, num):
    num = num % 26
    lowerCaseString = str.lower()
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    # or alphabet = list(string.ascii_lowercase)
    # or alphabet = list(map(chr, range(97, 123)))
    # or alphabet = list(map(chr, range(ord('a'), ord('z')+1)))

    # reverse the string
    #   string.ascii_lowercase[::-1]

    newString = ''
    for index in range(len(lowerCaseString)):
        currentLetter = lowerCaseString[index]
        if currentLetter == ' ':
            newString += currentLetter
            continue
        currentIndex = alphabet.index(currentLetter)
        newIndex = currentIndex + num
        if newIndex > 25:
            newIndex = newIndex - 26
        elif newIndex < 0:
            newIndex = newIndex + 26

        if str[index] == str[index].upper():
            newString += alphabet[newIndex].upper()
        else:
            newString += alphabet[newIndex]
    return newString

print(caesarCipher('Zoo Keeper ', 2)) # Bqq Mggrgy
print(caesarCipher('Big Car', -16)) # Lsq Mkb
print(caesarCipher('Javascript', -900)) # Tkfkcmbszd
