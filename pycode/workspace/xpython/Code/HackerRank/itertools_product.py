from itertools import product

both_lists = []
both_lists.append(list(map(int, input().split())))
both_lists.append(list(map(int, input().split())))

result = " ".join(map(str, (list(product(*both_lists)))))
print(result)
