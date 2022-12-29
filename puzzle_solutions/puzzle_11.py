from collections import deque
from dataclasses import dataclass
from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()


@dataclass
class Monkey:
    starting_items: deque[int]
    operation: str
    test: int
    if_true: int
    if_false: int

    def monkey_business(self) -> tuple[int, int]:
        worry: int = 0
        passed_to: int = 0

        return worry, passed_to


def generate_monkey(monkey_stats: list[str]) -> Monkey:
    starting_items: list[int] = [
        int(item) for item in monkey_stats[0].split(":")[1].split(",")
    ]
    operation = monkey_stats[1].split(":")[1]
    test = int(monkey_stats[2].split()[-1])
    if_true = int(monkey_stats[3].split()[-1])
    if_false = int(monkey_stats[4].split()[-1])
    return Monkey(deque(starting_items), operation, test, if_true, if_false)


def part_1(monkeys: list[Monkey]):
    # TODO Replace with solution
    pass


def part_2():
    # TODO Replace with solution
    pass


def main() -> None:
    monkeys: list[Monkey] = []
    for i, line in enumerate(INPUT):
        if line.startswith("Monkey"):
            monkeys.append(generate_monkey(INPUT[i + 1 : i + 6]))

    print(f"The answer to part 1 is {part_1(monkeys)}")
    print(f"The answer to part 2 is {part_2()}")


if __name__ == "__main__":
    main()
