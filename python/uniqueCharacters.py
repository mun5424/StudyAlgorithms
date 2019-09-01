# determine if a string has all unique characters

def uniqueCharacters(word):
    chars = [False] * 128
    for i in word: 
        letterIndex = ord(i)
        if chars[letterIndex]:
            return False
        else:
            chars[letterIndex] = True
    return True


    
    
        

print(uniqueCharacters('asdsadkjasxd')) # fail
print(uniqueCharacters('abcde')) # pass
