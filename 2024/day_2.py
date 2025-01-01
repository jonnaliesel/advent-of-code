from puzzle_input import get_puzzle_input

reports = get_puzzle_input("2")
result = 0
err = 0

for level in reports:
    parsed_level = list(map(int, level[0].split()))
    if  (all(i < j and j - i in [1, 2, 3] for i, j in zip(parsed_level, parsed_level[1:])) or
        all(i > j and i - j in [1, 2, 3] for i, j in zip(parsed_level, parsed_level[1:]))
        ):
        result += 1
    else:
        pass
print(result)
print(err)


