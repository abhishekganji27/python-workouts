
import random
def guessing_game_v1():
    ans = random.randint(0,100)
    guess = int(input("Guess the number: "))
    
    while chances > 0 and ans != guess:
        print(f"You guessed {guess}")
        res = "Too High" if ans < guess else "Too Low"
        print(f"{res}!...")
        guess = int(input("Guess the number: "))
        chances -= 1
    
    print(f"You guessed {guess}...Just Right!")
    
# guessing_game_v1()
#-----------------------------------------------------------

def guessing_game_v2():
    print(f"{"*"*5} Guessing Game {"*"*5}")
    chances = 3
    ans = random.randint(0,100)
    guess = int(input(f"You have {chances} chances left. Guess the number: "))
    
    while True:
        print(f"You guessed {guess}...")
        
        if ans == guess:
            print(f"Just Right!")
            break
        else:
            res = "Too High" if ans < guess else "Too Low"
            print(f"{res}!...")
        
            chances -= 1
            if chances == 0:
                print("You did not guess in time!")
                print(f"The answer was {ans}!")
                break
            
            guess = int(input(f"You have {chances} chances left. Guess the number: "))
    
# guessing_game_v2()
# --------------------------------------------------------

def decimal_to_hex(decimal_num):
    hex_digits = "0123456789ABCDEF"
    hex_num = ""
    duplicate_dn = decimal_num
    while decimal_num != 0:
        quo = decimal_num // 16
        rem = decimal_num % 16
        hex_num = hex_digits[rem] + hex_num
        decimal_num = quo
        
    # print(f"Hex value of decimal num {duplicate_dn} is {hex_num}")
    return hex_num
    
    
def hex_to_decimal(hex_str):
    hex_digits = "0123456789ABCDEF"
    hex_str = hex_str.upper()
    decimal_val = 0
    for i, digit in enumerate(reversed(hex_str)):
        decimal_val += hex_digits.index(digit) * (16 ** i)
    # return f"Decimal value of hex str {hex_str} is {decimal_val}"
    return decimal_val
   
# hex_num = decimal_to_hex(16)
# print(hex_to_decimal(hex_num)) 

def decimal_to_binary(decimal_num):
    binary_num = ""
    duplicate_dn = decimal_num
    while decimal_num != 0:
        bit = str(decimal_num % 2)
        binary_num = bit + binary_num
        decimal_num = decimal_num // 2
    # print(f"Decimal Value: {duplicate_dn} => Binary value : {binary_num}")
    return binary_num
    
def binary_to_decimal(binary_str):
    decimal_num = 0
    for i, bit in enumerate(reversed(binary_str)):
        decimal_num += int(bit) * (2 ** i)
    # return f"Binary Value: {binary_str} => Decimal value : {decimal_num}"
    return decimal_num
    
# binary_num = decimal_to_binary(25)
# print(binary_to_decimal(binary_num))
    
def guessing_game_v3():
    # choose random number
    ans = random.randint(0,100)
    # choose base of random number
    r_base = random.choice([2,10,16])
    
    print(f"{"*"*5} Guessing Game {"*"*5}")
    chances = 3
    user_prompt = f"You have {chances} chances. Guess the number in base {r_base}: "
    guess = input(user_prompt)
    
    while True:
        print(f"You guessed {guess}...")
        adj_guess = -1
        if r_base == 2:
            adj_guess = binary_to_decimal(guess)
        elif r_base == 16:
            adj_guess = hex_to_decimal(guess)
        else: 
            adj_guess = int(guess)
            
        if ans == adj_guess:
            print(f"Just Right!")
            break
        else:
            res = "Too High" if ans < adj_guess else "Too Low"
            print(f"{res}!...")
        
            chances -= 1
            if chances == 0:
                print("You did not guess in time!")
                print(f"The answer was {ans}!")
                break
            
            guess = input(f"You have {chances} chances. Guess the number in base {r_base}: ")

# guessing_game_v3()  
# --------------------------------------------------------
"""
have the program choose a random word from the dictionary and then ask the user to guess the word. (You might want to limit yourself to words containing two to five letters to avoid making it too horribly difficult.) Instead of telling the user that they should guess a smaller or larger number, have them choose an earlier or later word.
"""

def guessing_game_v4():
    # get random word from dictionary
    from wonderwords import RandomWord
    r = RandomWord() 
    ans = r.word(word_min_length=2, word_max_length=5)
    # print("Ans is : ", ans)
    
    # spellcheck
    import enchant
    d = enchant.Dict("en_US")

    # print(d.check("Hello")) prints True
    # print(d.check("Helo"))  prints False

    print(f"{"*"*5} Guessing Game {"*"*5}")
    chances = 3
    user_prompt = f"You have {chances} chances to guess the {len(ans)}-letter word. Guess the word: "
    guess = input(user_prompt)
    
    while True:
        print(f"Your guess: {guess}")
        
        if ans == guess:
            print(f"Just Right!")
            break

        if not d.check(guess):
            print("Please input a valid English word as your guess.")

        elif len(ans) != len(guess):
            print(f"Your guess was a {len(guess)}-letter word. Please guess a {len(ans)}-letter word.")

        else:
            for i in range(len(guess)):
                if ord(guess[i]) > ord(ans[i]):
                    print(f"Guess an earlier word.")
                    break
                elif ord(guess[i]) < ord(ans[i]):
                    print(f"Guess a later word.")
                    break
            
        
        chances -= 1
        if chances == 0:
            print("You did not guess in time!")
            print(f"The answer was {ans}!")
            break

        user_prompt = f"You have {chances} chance{"s" if chances > 1 else ""} to guess the {len(ans)}-letter word. Guess the word: "
        guess = input(user_prompt)

guessing_game_v4()  

    
    