def mysum_v1(*nums, starting_point=0):
    output = 0
    for n in nums:
        output += n
    return output + starting_point

# print(mysum_v1(1,2,3))
# print(mysum_v1(*(1,2,3), 1))
# print(mysum_v1(*[1,2,3]))
# print(mysum_v1(*[1,2,3], 4))

#-----------------------------------------------

def avg_of_nums(*nums):
    s = 0
    for n in nums:
        s += n
    return s/len(nums)
    
# print("avg: ", avg_of_nums(*[1,2,3,4]))
#-----------------------------------------------

def avg_words(*strings):
    avg_len = 0
    smallest = 10000000
    largest = 0
    empty = 0
    for s in strings:
        if s == "":
            empty += 1
        else:
            avg_len += len(s)
            smallest = min(smallest, len(s))
            largest = max(largest, len(s))

    # to avoid division by zero error.
    if len(strings) != empty: 
        avg_len = avg_len / len(strings) - empty

    return (smallest, largest, avg_len)

# print("Avg words: ", avg_words(*["hi", "hello", "what"]))
# Avg words:  (2, 5, 3.6666666666666665)
# print("Avg words: ", avg_words(*["", "", ""]))
#-----------------------------------------------

def sum_of_ints(*objs):
    ans = 0
    for obj in objs:
        try: 
            new_obj = int(obj)
            ans += new_obj
        except:
            print("nay: ", obj)
            continue
    return ans

# print("Ans: ", sum_of_ints(1,2, "3", True, None, [1,2], False))