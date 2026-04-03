def mysum_v1(*nums, starting_point=0):
    output = 0
    for n in nums:
        output += n
    return output + starting_point

print(mysum_v1(1,2,3))
print(mysum_v1(*(1,2,3), 1))
print(mysum_v1(*[1,2,3]))
print(mysum_v1(*[1,2,3], 4))