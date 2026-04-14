import re
sum_of_games = 0
balls = {"red": 12, "green": 13, "blue": 14}

filename = "input.txt"
input = []
with open(filename) as file:
    # till line 21  the code creates a list of dictionaries like with blue, green read as keys and 
    # the amount of each of them 
    no_re_line = [line.strip() for line in file.readlines()]
    for item in no_re_line:
        item = re.sub(r"Game\s\d+:\s", "", item)
        item = item.split("; ")
        for i in range(len(item)):
            k = item[i].split(" ")
            for x in range(len(k)):
                if "," in k[x]:
                    a = k[x].replace(",", "")
                    k[x] = a
            y = dict(zip(k[1::2], k[::2]))
            item[i] = y
        input.append(item)
flag = False
for i, c in enumerate(input):
    for inning in c:                                    # every dictionary on the list 
        if not flag:
            compare_keys = inning.keys() & balls.keys()  # set of keys of the comparing dictionaries 
            for key in compare_keys:
                if int(inning.get(key)) > balls.get(key): # must convert to int the value which was originally a sting type
                    flag = True
                    break
                else:
                    continue

    if not flag:
        sum_of_games += i + 1        
        
    flag = False        
        
print(sum_of_games)
