def isPalindrome(str):
    string = str.lower()
    charactersArr = list(string)
    validCharacters = list('abcdefghijklmnopqrstuvwxyz')

    lettersArr = []
    for char in charactersArr:
        try:
            if(validCharacters.index(char)):
                lettersArr.append(char)
        except ValueError:
            pass
    if lettersArr == lettersArr[::-1]:
        print('yes')
    else:
        print('no')

isPalindrome("Madam I'm Adam")
isPalindrome("race car")
isPalindrome("Coding JavaScript")
