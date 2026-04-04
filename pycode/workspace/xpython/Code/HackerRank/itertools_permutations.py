from itertools import permutations

input = input().split()
word, r = input[0], input[1]

perm_sorted_list = sorted(list(permutations(word, int(r))))
for x in range(len(perm_sorted_list)):
    print("".join(perm_sorted_list[x]))
