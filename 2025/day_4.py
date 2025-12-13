"""Advent of Code 2025 - Day 4: Rolls of paper

The elves need to move rolls of paper from the warehouse.

Part 1:
Forklifts can only
access rolls that have fewer than 4 adjacent rolls (considering all 8 neighbors:
horizontal, vertical, and diagonal).
"""

from puzzle_input import get_puzzle_input_string

# Constants
DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
MAX_NEIGHBORS = 4
PAPER_ROLL = '@'

def build_grid(diagram: str) -> dict:
    """Parse diagram string into a grid dictionary.
    
    Args:
        diagram: Multi-line string representing the warehouse layout.
    
    Returns:
        Dictionary mapping (row, col) positions to characters.
    """
    return {
        (row, col): char
        for row, line in enumerate(diagram.split('\n'))
        for col, char in enumerate(line)
    }

def find_accessible_positions(grid: dict) -> list[tuple[int, int]]:
    """Find all paper roll positions that are accessible by forklifts.
    
    A roll is accessible if it has fewer than {MAX_NEIGHBORS} adjacent rolls in the
    8 surrounding positions (horizontal, vertical, and diagonal).
    
    Args:
        grid: Dictionary mapping (row, col) tuples to characters.
    
    Returns:
        List of (row, col) tuples for accessible positions.
    """
    accessible = []
    
    for position, char in grid.items():
        if char != PAPER_ROLL:
            continue
            
        row, col = position
        neighbor_count = sum(
            1 for dr, dc in DIRECTIONS
            if (row + dr, col + dc) in grid
            and grid[(row + dr, col + dc)] == PAPER_ROLL:
        )
        
        if neighbor_count < MAX_NEIGHBORS:
            accessible.append(position)
    
    return accessible

def simulate_removal(grid: dict) -> int:
    """Remove accessible rolls iteratively until none remain.
    
    Args:
        grid: Dictionary mapping (row, col) tuples to characters.
              Will be modified by this function.
    
    Returns:
        Total number of rolls removed across all iterations.
    """
    total_removed = 0
    
    while True:
        to_remove = find_accessible_positions(grid)
        if not to_remove:
            break
        
        for pos in to_remove:
            del grid[pos]
        
        total_removed += len(to_remove)
    
    return total_removed

def main():
    """Solve both parts of Day 4."""
    diagram = get_puzzle_input_string("4")
    grid = build_grid(diagram)
    
    part1_answer = len(find_accessible_positions(grid))
    part2_answer = simulate_removal(grid)
    
    print(f"Part 1: {part1_answer}")
    print(f"Part 2: {part2_answer}")


# Tests
def test_part1():
    """Test part 1 with example data."""
    test_diagram = get_puzzle_input_string("4_test")
    grid = build_grid(test_diagram)
    assert len(find_accessible_positions(grid)) == 13

def test_part2():
    """Test part 2 with example data."""
    test_diagram = get_puzzle_input_string("4_test")
    grid = build_grid(test_diagram)
    assert simulate_removal(grid) == 43

if __name__ == "__main__":
    main()
