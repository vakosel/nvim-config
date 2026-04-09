from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:

    # your code here
    text += "_" * (len(text) % 2)

    return [text[i : i + 2] for i in range(0, len(text), 2)]


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
