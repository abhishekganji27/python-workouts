def pig_latin(word):
    
    if word[0] in 'aeiou':
        return word[1:] + "way" 
    return word[1:] + word[0] + "ay"

print(pig_latin("apple")) #return ppleway
print(pig_latin("computer")) # returns omputercay