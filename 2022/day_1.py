from ..puzzle_input import get_puzzle_input

all_elves = get_puzzle_input(1)


def get_elf_with_most_calories(all_elves):
    elves = []
    elf_with_most = 0
    calories = 0
    for snack in all_elves:
        if not snack == "\n":
            calories += int(snack)
        else:
            elves.append(calories)
            if calories > elf_with_most:
                elf_with_most = calories
            calories = 0
    elves.sort(reverse=True)
    print(elves[0:3])
    return (elf_with_most, (elves[0] + elves[1] + elves[2]))


print(get_elf_with_most_calories(all_elves))
