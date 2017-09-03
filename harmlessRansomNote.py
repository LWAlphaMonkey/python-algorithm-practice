def harmlessRansomNote(note, magazineNote):
    magazineArr = magazineNote.split()
    noteArr = note.split()
    magazineObj = {}

    for word in magazineArr:
        if magazineObj.get(word) == None:
            magazineObj[word] = 0
        magazineObj[word] += 1

    noteIsPossible = True

    for word in noteArr:
        if magazineObj.get(word):
            magazineObj[word] -= 1
            if magazineObj[word] < 0:
                noteIsPossible = False
        else:
            noteIsPossible = False
    return noteIsPossible

print(harmlessRansomNote('hello there', 'hello do you want to do some exercise'))
