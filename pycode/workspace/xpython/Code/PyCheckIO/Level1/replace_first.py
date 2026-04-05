from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    return items[1:] + items[:1] if items else items


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))
print(replace_first([1]))
print(replace_first([]))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
