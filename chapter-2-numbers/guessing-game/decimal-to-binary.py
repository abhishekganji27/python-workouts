def decimal_to_binary(decimal_num):
    binary_num = ""
    duplicate_dn = decimal_num
    while decimal_num != 0:
        bit = str(decimal_num % 2)
        binary_num = bit + binary_num
        decimal_num = decimal_num // 2
    print(f"Decimal Value: {duplicate_dn} => Binary value : {binary_num}")
    return binary_num
    
def binary_to_decimal(binary_str):
    decimal_num = 0
    for i, bit in enumerate(reversed(binary_str)):
        decimal_num += int(bit) * (2 ** i)
    return f"Binary Value: {binary_str} => Decimal value : {decimal_num}"
    # return decimal_num
    
binary_num = decimal_to_binary(int(input("Enter decimal number: ")))
print(binary_to_decimal(binary_num))