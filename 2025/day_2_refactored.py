"""Advent of Code 2025 - Day 2: Invalid ID Detection

This module finds "invalid" IDs that consist of repeated patterns.
For example: 123123 (123 repeated twice), 55 (5 repeated twice).
"""

from puzzle_input import get_puzzle_input_string


def parse_ranges(input_string: str) -> list[tuple[int, int]]:
    ranges = []
    for range_str in input_string.split(","):
        start, end = map(int, range_str.split("-"))
        ranges.append((start, end))
    return ranges


def has_repeating_pattern(number: int, check_all_patterns: bool = False) -> bool:
    num_str = str(number)
    max_repetitions = len(num_str) + 1 if check_all_patterns else 3
    
    for repetitions in range(2, max_repetitions):
        if len(num_str) % repetitions != 0:
            continue
        
        pattern_length = len(num_str) // repetitions
        pattern = num_str[:pattern_length]
        
        if pattern * repetitions == num_str:
            return True
    
    return False


def find_invalid_ids(ranges: list[tuple[int, int]], part2: bool = False) -> int:
    total = 0
    for start, end in ranges:
        for num in range(start, end + 1):
            if has_repeating_pattern(num, check_all_patterns=part2):
                total += num
    return total


def main():
    input_data = get_puzzle_input_string("2")
    ranges = parse_ranges(input_data)
    
    part1_answer = find_invalid_ids(ranges, part2=False)
    part2_answer = find_invalid_ids(ranges, part2=True)
    
    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


# Tests
def test_part1():
    """Test part 1 with example data."""
    test_input = get_puzzle_input_string("2_test")
    test_ranges = parse_ranges(test_input)
    assert find_invalid_ids(test_ranges, part2=False) == 1227775554


def test_part2():
    """Test part 2 with example data."""
    test_input = get_puzzle_input_string("2_test")
    test_ranges = parse_ranges(test_input)
    assert find_invalid_ids(test_ranges, part2=True) == 4174379265


if __name__ == "__main__":
    main()
