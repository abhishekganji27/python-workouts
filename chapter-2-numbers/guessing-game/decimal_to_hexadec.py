def decimal_to_hex(decimal_num):
    hex_digits = "0123456789ABCDEF"
    hex_num = ""
    duplicate_dn = decimal_num
    while decimal_num != 0:
        quo = decimal_num // 16
        rem = decimal_num % 16
        hex_num = hex_digits[rem] + hex_num
        decimal_num = quo
        
    print(f"Decimal num: {duplicate_dn} => Hex value: {hex_num}")
    return hex_num
    
    
def hex_to_decimal(hex_str):
    hex_digits = "0123456789ABCDEF"
    hex_str = hex_str.upper()
    decimal_val = 0
    for i, digit in enumerate(reversed(hex_str)):
        decimal_val += hex_digits.index(digit) * (16 ** i)
    return f"Hex Value: {hex_str} => Decimal value : {decimal_val}"
    # return decimal_val
   
hex_num = decimal_to_hex(int(input("Enter decimal number: ")))
print(hex_to_decimal(hex_num)) 