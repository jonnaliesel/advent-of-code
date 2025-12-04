from puzzle_input import get_puzzle_input_string

id_ranges = get_puzzle_input_string("2").split(",")
id_ranges_test = get_puzzle_input_string("2_test").split(",")

def find_and_sum_invalid_ids(id_ranges:list[str]) -> int:
    sum = 0
    for id_range in id_ranges:
        start, end = id_range.split("-")
        start = int(start)
        end = int(end)

        for id in range(start, end+1):
            if len(str(id)) % 2 != 0:
                continue
            else: 
                seq_length = len(str(id)) // 2
                if str(id)[:seq_length] == str(id)[seq_length:]:
                    sum += id

    return sum

def test_answer_1():
    assert find_and_sum_invalid_ids(id_ranges_test) == 1227775554

if __name__ == "__main__":
    print(find_and_sum_invalid_ids(id_ranges))
    # print("Passcode 1: " + str(get_passcode_1(rotation_instructions)))
    # print("Passcode 2: " + str(get_passcode_2(rotation_instructions)))
