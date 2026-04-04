def print_formatted(number):
    # your code goes here
    spaces = len(format(number, "b"))
    for i in range(1, number + 1):
        int_values = []
        int_values.append(str(i))
        int_values.append(format(i, "o"))
        int_values.append(format(i, "x".upper()))
        int_values.append(format(i, "b"))
        formatted_numbers = [f"{n:>{spaces}}" for n in int_values]
        print(" ".join(formatted_numbers))


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
