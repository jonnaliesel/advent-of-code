from day_2 import play_rock_paper_scissor

test_data = "A Y", "B X", "C Z"


def test_day_two():
    assert play_rock_paper_scissor(test_data) == (15, 12)
