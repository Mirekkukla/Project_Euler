count = 0
num_array = [0,1,2,3,4,5,6,7,8,9]
array_len = len(num_array)

def recurse(left_string, x):
    global count
    if len(left_string) == array_len:
        count += 1
        if count == 1000000: print(left_string)
    else:
        for i in x:
            x_copy = [] + x
            x_copy.remove(i)
            recurse(left_string + str(i), x_copy)

recurse('',num_array)