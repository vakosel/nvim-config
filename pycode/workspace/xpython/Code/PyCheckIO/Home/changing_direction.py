def changing_direction(elements: list[int]) -> int:
    # your code here
    changes = 0
    direction = None
    for i in range(1, len(elements)):
        if elements[i] > elements[i - 1]:
            if direction == "down":
                changes += 1
            direction = "up"
        elif elements[i] < elements[i - 1]:
            if direction == "up":
                changes += 1
            direction = "down"

    return changes


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
assert changing_direction([1, 2, 2, 2, 1, 2]) == 2


print("The mission is done! Click 'Check Solution' to earn rewards!")
