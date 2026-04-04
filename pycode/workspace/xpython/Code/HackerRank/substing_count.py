def count_substring(string, sub_string):
    flag = True
    count = 0
    while flag:
        a = string.find(sub_string)
        if a == -1:
            flag = False
        else:
            count += 1
            string = string[a + 1 :]
    return count


count = count_substring("abcdcdc", "cdc")
print(count)
