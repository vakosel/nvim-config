def average(array):
    # your code goes here
    my_set = set(array)
    length = len(my_set)
    return sum(my_set) / length


arr = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
result = average(arr)
print(result)
