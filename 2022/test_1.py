from day_1 import get_elf_with_most_calories

test_data = [
    "1000",
    "2000",
    "3000",
    "\n",
    "4000",
    "5000",
    "6000",
    "\n",
    "7000",
    "8000",
    "9000",
    "\n",
    "10000",
]


def test_day_one():
    assert get_elf_with_most_calories(test_data) == (24000, 45000)
