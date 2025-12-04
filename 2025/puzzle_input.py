def get_puzzle_input1(day: str) -> list[str]:
    with open(f"{day}.txt", "r") as f:
        return [line.split() for line in f]

def get_puzzle_input(day: str) -> list[str]:
    with open(f"{day}.txt", "r") as f:
        return [line.rstrip() for line in f]

def get_puzzle_input_string(day: str) -> str:
    with open(f"{day}.txt", "r") as f:
        return f.read()
