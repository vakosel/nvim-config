import re
sum_of_games = 0

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
        result = [{k: int(v) for k, v in d.items()} for d in map(lambda x: dict(x), item)] 
        input.append(result)

for lst in input:
    all_keys = set().union(*lst)  #  set of keys o) 
    max_values = {key: max(dic.get(key, float('-inf')) for dic in lst) for key in all_keys}    
    multi = max_values['red'] * max_values['blue'] * max_values['green']
    sum_of_games += multi
        
print(sum_of_games)
            
            
   
