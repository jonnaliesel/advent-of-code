from puzzle_input import get_puzzle_input1

lists = get_puzzle_input1("1")
list1 = []
list2 = []
total_distance = 0

for obj in lists:
    list1.append(int(obj[0]))
    list2.append(int(obj[1]))

list1 = sorted(list1)
list2 = sorted(list2)

dest = map(lambda x, y: abs(x - y), list1, list2)

for l in list(dest):
    total_distance += l

print(f"Part one: {total_distance}")

similarity_score = 0

for x in list1:
    similarity_score += list2.count(x) * x

print(f"Part 2: {similarity_score}")