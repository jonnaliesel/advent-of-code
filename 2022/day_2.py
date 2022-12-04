from puzzle_input import get_puzzle_input

strategy = get_puzzle_input(2)


def play_rock_paper_scissor(strategy):
    points_one = 0
    points_two = 0
    elves_hands = {"A": 1, "B": 2, "C": 3}
    your_hands = {"X": 1, "Y": 2, "Z": 3}
    for game in strategy:
        play = game.strip().split(" ")
        elf, you = [play[0], play[1]]
        if elves_hands[elf] == your_hands[you]:
            points_one += 3 + your_hands[you]
        elif (
            elves_hands[elf] - your_hands[you] == 2
            or your_hands[you] - elves_hands[elf] == 1
        ):
            points_one += 6 + your_hands[you]
        else:
            points_one += your_hands[you]

        your_hands_values = list(your_hands.values())
        if you == "X":
            loose = abs(elves_hands[elf] + 1) % 3
            points_two += your_hands_values[loose]
            print(f"Loose: {elf} Points: {your_hands_values[loose]}")
        elif you == "Y":
            points_two += 3 + elves_hands[elf]
            print(f"Draw: {elf} Points: {3 + elves_hands[elf]}")
        elif you == "Z":
            win = (elves_hands[elf] + 3) % 3
            points_two += 6 + your_hands_values[win]
            print(f"Win: {elf} Points: {6 + your_hands_values[win]}")

    return (points_one, points_two)


print(play_rock_paper_scissor(strategy))
