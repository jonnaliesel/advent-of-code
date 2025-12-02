from puzzle_input import get_puzzle_input

rotation_instructions = get_puzzle_input("1")
rotation_instructions_test = get_puzzle_input("1_test")

def get_passcode_1(rotation_instructions: list[str]) -> int:
    current = 50
    passcode = 0
    for instruction in rotation_instructions:
        direction = instruction[0]
        rotations = int(instruction[1:])
        if direction == "R":
            current = (current + rotations) % 100
            if current == 0:
                passcode += 1
        elif direction == "L":
            current = (current - rotations) % 100
            if current == 0:
                passcode += 1

    return passcode

def get_passcode_2(rotation_instructions: list[str]) -> int:
    current = 50
    passcode = 0
    for instruction in rotation_instructions:
        direction = instruction[0]
        rotations = int(instruction[1:])
        if direction == "R":
            new_position = current + rotations
            passages = (new_position - 1) // 100 - (current - 1) // 100
            current = new_position % 100
            passcode += passages
        elif direction == "L":
            new_position = current - rotations
            passages = (current - 1) // 100 - (new_position - 1) // 100
            current = new_position % 100
            passcode += passages
    return passcode

def test_answer_1():
    assert get_passcode_1(rotation_instructions_test) == 3

def test_answer_2():
    assert get_passcode_2(rotation_instructions_test) == 6

if __name__ == "__main__":
    print("Passcode 1: " + str(get_passcode_1(rotation_instructions)))
    print("Passcode 2: " + str(get_passcode_2(rotation_instructions)))
