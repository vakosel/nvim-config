import re


def backward_string_by_word(text: str) -> str:
    # your code here
    pattern = r"\w+|\s+"
    matches = re.findall(pattern, text)
    new_string = "".join(match[::-1] if match.strip() else match for match in matches)

    return new_string


print("Example:")
print(backward_string_by_word(""))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
