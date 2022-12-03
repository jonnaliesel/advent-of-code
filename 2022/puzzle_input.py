def get_puzzle_input(day: int) -> list[str]:
    return [line for line in open(f"{day}.txt", "r").readlines()]
