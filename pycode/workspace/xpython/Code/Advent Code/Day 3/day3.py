import re

filename = "example.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

digit_spans = []
symbols_idx = []
digit_numbers = []

for line in input:
    digit_spans.append([m.span() for m in re.finditer(r"\d+", line)])
    digit_numbers.append(re.findall(r"\d+", line))
    symbols_idx.append(
        [m.start() for m in re.finditer(r"[@_!$%^&*()<>?/\|}{~:#]", line)]
    )

# def get_adjacent_cells(digit_start, digit_end, y_coord ):
#     result = {}
#     for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
#         if (x,y) in grid.cells:
#             result[(x,y)] = grid.cells[(x,y)]
print(digit_numbers)
print(symbols_idx)
