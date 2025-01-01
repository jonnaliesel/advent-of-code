def get_puzzle_input1(day: str) -> list[str]:
    ret = []
    for line in open(f"{day}.txt", "r"):
        ret.append([line.split()[0], line.split()[1].rstrip()])
    return ret

def get_puzzle_input(day: str) -> list[str]:
    ret = []
    for line in open(f"{day}.txt", "r"):
        ret.append([line.rstrip()])
    return ret
