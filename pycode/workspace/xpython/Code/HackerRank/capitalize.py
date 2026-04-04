def solve(s):
    wordws = s.split(" ")
    wordws1 = (i.capitalize() for i in wordws)
    return " ".join(wordws1)


if __name__ == "__main__":
    s = input()
    result = solve(s)
    print(result)
