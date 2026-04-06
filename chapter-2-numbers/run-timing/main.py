def run_timing():
    cnt = 0
    total = 0
    while True:
        run_time = input("Enter 10km run time: ")
        if not run_time:
            break
        try:
            total += float(run_time)
            cnt += 1
        except: 
            break
    print(f"Average of {total/cnt:.1f}, over {cnt} runs")
    
# run_timing()

#-----------------------------

def float_formatting(num, before, after):
    return f"{num % (10**before):.{after}f}"

# print(float_formatting(1234.56790,2,3)) #prints 34.568 
# print(float_formatting(1234.56790,5,3)) #prints 1234.568 
# print(float_formatting(1234.56790,3,1)) #prints 234.6

#-----------------------------
"""
Floating point numbers whose denom is not a power of 2 are not stored precisely by the computer. 
0.1 (decimal) = 1/10
In binary, it becomes an infinite repeating fraction:
0.1 (decimal) = 0.0001100110011001100110011... (binary)
                         ↑ repeating "0011"

Binary uses powers of 2:

1/2 = 0.1 ✅
1/4 = 0.01 ✅

But:
1/10 ❌ → can't be expressed as sum of powers of 2
→ so it becomes infinite repeating, like 1/3 = 0.333... in decimal

Since computer can't store infinite digits, it cuts it off:

Stored value of 0.1 ≈ 0.0001100110011001100110011001100 (truncated) 
(approx binary representation is stored)

Converted back to decimal:

0.1 ≈ 0.10000000000000000555... 
In simple words, numbers are stored slightly wrong. 

"""
def decimal_add(a, b):
    import decimal
    d = decimal.Decimal
    print(f"\na = {a}, b = {b}")
    return f"normal add res: {float(a) + float(b)}\ndecimal add res: {d(a) + d(b)}"

print(decimal_add('0.1', '0.2')) 
print(decimal_add('0.3', '0.2')) 
print(decimal_add('0.1', '0.7'))

#-----------------------------
