# ? COPY ME FOR EACH PUZZLE
from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()

def part_1():
    # TODO Replace with solution
    pass

def part_2():
    # TODO Replace with solution
    pass


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")

if __name__ == "__main__":
    main()