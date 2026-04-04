from collections import Counter

num_of_shoes = int(input())
shoes = list(map(int, input().split()))

counter = Counter(shoes)

customer_count = int(input())
total_amount = 0
for _ in range(customer_count):
    size, price = map(int, input().split())
    if counter[size] > 0:
        counter[size] -= 1
        total_amount += price
    else:
        pass

print(total_amount)
