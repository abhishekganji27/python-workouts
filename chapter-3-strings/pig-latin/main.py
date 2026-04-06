def pig_latin_v1(word):
    
    if word[0] in 'aeiou':
        return word + "way" 
    return word[1:] + word[0] + "ay"

# print(pig_latin_v1("apple")) #return appleway
# print(pig_latin_v1("eat")) #return eatway
# print(pig_latin_v1("python")) #return ythonpay
# print(pig_latin_v1("computer")) # returns omputercay

#-----------------------------------
"""
(Initial Messy Approach)
def pig_latin_v2(word):
    capitalized = False 
    if word[0].isupper() and word[1:].islower(): 
        capitalized = True 

    if word[0].lower() in 'aeiou': 
        return word + "way" 

    if capitalized: 
        return word[1].upper() + word[2:] + word[0].lower() + "ay" 
        
    return word[1:] + word[0] + "ay"

print(pig_latin_v2("apple")) #returns appleway
print(pig_latin_v2("Apple")) #returns Appleway
print(pig_latin_v2("computer")) # returns omputercay
print(pig_latin_v2("Computer")) # returns Omputercay
print(pig_latin_v2("hi")) # returns ihay
print(pig_latin_v2("Hi")) # returns Ihay

Clear separation, instead of mixing steps:
1. Normalize. Convert word to lowercase.
2. Transform. Manipulate string as per rules.
3. Capitalization. If applicable, perform at the end.
"""

def pig_latin_v2(word):
    capitalized = word[0].isupper() and word[1:].islower()
    #1
    word_l = word.lower() 
    #2
    if word_l[0] in 'aeiou':
        res = word_l + "way"
    else: 
        res = word_l[1:] + word_l[0] + "ay"
    #3
    if capitalized:
        return res.capitalize()
    return res

# print(pig_latin_v2("apple")) #returns appleway
# print(pig_latin_v2("Apple")) #returns Appleway
# print(pig_latin_v2("computer")) # returns omputercay
# print(pig_latin_v2("Computer")) # returns Omputercay
# print(pig_latin_v2("hi")) # returns ihay
# print(pig_latin_v2("Hi")) # returns Ihay

#-----------------------------------

def pig_latin_v3(word):
    punctuations = ['.', ',', '!', '?', '...', ':', ';', "'", '-']
    p_idx = -1
    for i, p in enumerate(punctuations):
        if word.endswith(p):
            p_idx = i
    
    capitalized = word[0].isupper() and word[1:].islower()
    wl = word.lower() if p_idx == -1 else word[:-len(punctuations[p_idx])].lower()
    if wl[0] in 'aeiou':
        res = wl + "way"
    else:
        res = wl[1:] + wl[0] + "ay"
    
    if capitalized:
        res = res.capitalize()
    
    if p_idx != -1:
        res += punctuations[p_idx]
    
    return res

# print(pig_latin_v3("apple.")) #returns appleway.
# print(pig_latin_v3("Apple;")) #returns Appleway;
# print(pig_latin_v3("computer?")) # returns omputercay?
# print(pig_latin_v3("Computer,")) # returns Omputercay,
# print(pig_latin_v3("hi'")) # returns ihay'
# print(pig_latin_v3("hello...")) # returns ellohay...
# print(pig_latin_v3("Hi!")) # returns Ihay!

#-----------------------------------

def pig_latin_v4(word):
    vowels_set = set()
    
    for c in word.lower():
        # char is vowel
        if c in 'aeiou':
            # add char to set
            vowels_set.add(c)
            # found atleast 2 vowels?
            if len(vowels_set) == 2:
                break

    if len(vowels_set) == 2:
        return word + "way"
    
    return word[1:] + word[0] + "ay"
