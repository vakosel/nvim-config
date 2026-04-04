rows, length = map(int, input().split())

pat1 = ".|."

odd_number = [num for num in range(1, rows) if num % 2 != 0]

for i in odd_number:
    print((pat1 * i).center(length, "-"))

print("WELCOME".center(length, "-"))

for i in reversed(odd_number):
    print((pat1 * i).center(length, "-"))
