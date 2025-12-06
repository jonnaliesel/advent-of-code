"""Advent of Code 2025 - Day 3: Maximum Joltage


"""

from puzzle_input import get_puzzle_input

def find_batteries(bank:str, part_2: bool = False) -> int:
    batteries = ""
    position = 0
    
    target_length = 12 if part_2 else 2
    while len(batteries) < target_length:
        remaining_needed = target_length - len(batteries)
        search_end = len(bank) - remaining_needed + 1

        max_joltage = max(bank[position:search_end])
        position = bank.index(max_joltage, position)

        batteries += bank[position]
        position += 1

    return int(batteries)

def find_max_joltage(battery_banks:list[str], part_2:bool = False) -> int:
    joltage = 0

    for bank in battery_banks:
        joltage += find_batteries(bank, part_2)

    return joltage

def main():
    battery_banks = get_puzzle_input("3")

    part1_answer = find_max_joltage(battery_banks)
    part2_answer = find_max_joltage(battery_banks, True)
    
    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


# Tests
def test_part1():
    """Test part 1 with example data."""
    test_battery_banks = get_puzzle_input("3_test")
    assert find_max_joltage(test_battery_banks) == 357

def test_part2():
    """Test part 2 with example data."""
    test_battery_banks = get_puzzle_input("3_test")
    assert find_max_joltage(test_battery_banks, True) == 3121910778619

if __name__ == "__main__":
    main()
