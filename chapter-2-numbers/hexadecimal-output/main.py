"""
int function takes 2 args: char and base. char is the literal to be converted into integer. base indicates the base of the char. default base = 10
signature: int(char, base)
both int('5', 16) and int('5') return same result i.e. 5. 
int('A', 16) returns 10. 
int('A') returns error saying 'A' is invalid literal for base 10 

https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/ 

"""
def hex_to_decimal(hex_str):
    decimal_val = 0
    for i, c in enumerate(reversed(hex_str)):
        int_c = int(c, 16) 
        decimal_val += (16 ** i) * int_c
    return decimal_val

# hex_str="60"
# print(hex_to_decimal(hex_str))
# hex_str="A45"
# print(hex_to_decimal(hex_str))
# hex_str="AB"
# print(hex_to_decimal(hex_str))

#-----------------------------
""" reimplementation of hex_to_decimal without using int() """

def hex_to_dec_v2(hex_str):
    decimal_val = 0
    i = 0
    for c in reversed(hex_str):
        # val = -1
        if '0' <= c <= '9':
            val = ord(c) - ord('0')
        elif 'A' <= c <= 'F':
            val = ord(c) - ord('A') + 10
        elif 'a' <= c <= 'f':
            val = ord(c) - ord('a') + 10

        else: 
            print("invalid character: ", c)
            continue
        # if val != -1:
        decimal_val += (16 ** i) * val 
        i += 1
    
    return decimal_val

# hex_str="60" # ans = 96
# print(hex_to_dec_v2(hex_str))
# hex_str="E1" # ans = 225
# print(hex_to_dec_v2(hex_str))
# hex_str="AB" # ans = 171
# print(hex_to_dec_v2(hex_str))
# hex_str="A!B!@Z" # ans = 171
# print(hex_to_dec_v2(hex_str))
#-----------------------------

def name_triangle_v1():
    name = input("Enter your name: ")
    for i in range(len(name)):
        for j in range(i+1):
            print(name[j], end="")
        print()
    
# name_triangle_v1()

def name_triangle_v2():
    name = input("Enter your name: ")
    for i in range(len(name)):
        print(name[:i+1])
    
# name_triangle_v2()

def name_triangle_v3():
    name = input("Enter your name: ")
    temp = ""
    for ch in name:
        temp += ch
        print(temp)
    
# name_triangle_v3()

#-----------------------------