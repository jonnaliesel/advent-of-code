from puzzle_input import get_puzzle_input_string

id_ranges = get_puzzle_input_string("2").split(",")
id_ranges_test = get_puzzle_input_string("2_test").split(",")

def id_validation(id: int, p2: bool) -> bool:
    id_str = str(id)

    for k in range(2, len(id_str) + 1 if p2 else 3):
        if len(id_str) % k != 0:
            continue
        
        segment_size = len(id_str) // k
        first_segment = id_str[:segment_size]
        
        all_match = True
        for i in range(0, len(id_str), segment_size):
            if id_str[i:i + segment_size] != first_segment:
                all_match = False
                break
        
        if all_match:
            return True
    
    return False


def find_and_sum_invalid_ids(id_ranges:list[str], p2:bool) -> int:
    sum = 0
    for id_range in id_ranges:
        start, end = id_range.split("-")
        start = int(start)
        end = int(end)

        for id in range(start, end+1):
            if id_validation(id, p2):
                sum += id

    return sum

def test_answer_1():
    assert find_and_sum_invalid_ids(id_ranges_test, False) == 1227775554

def test_answer_2():
    assert find_and_sum_invalid_ids(id_ranges_test, True) == 4174379265

if __name__ == "__main__":
    print(find_and_sum_invalid_ids(id_ranges, False))
    print(find_and_sum_invalid_ids(id_ranges, True))
