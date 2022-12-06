from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)[0]  # * Only one line in puzzle input
logger = get_logger()


def find_first_x_distinct(length: int, data: str) -> int:
    for i in range(length, len(data)):
        if len(set(data[i - length : i])) == length:
            return i
    return -1


def part_1():
    return find_first_x_distinct(4, INPUT)


def part_2():
    return find_first_x_distinct(14, INPUT)


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")


if __name__ == "__main__":
    main()
