from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()


def get_elves() -> list[int]:
    elves: list[int] = []
    current_calories = 0
    for line in INPUT:
        if line:
            current_calories += int(line)
        else:
            elves.append(current_calories)
            current_calories = 0
    elves.append(current_calories)

    return elves


def part_1() -> int:
    elves: list[int] = get_elves()
    elf_with_most = 0
    for i, elf in enumerate(elves):
        if elves[elf_with_most] < elf:
            elf_with_most = i
    return elves[elf_with_most]


def part_2() -> int:
    elves: list[int] = get_elves()
    three_with_most: dict[int, int] = {1: 0, 2: 0, 3: 0}
    for i, elf in enumerate(elves):
        if i % 100 == 0:
            logger.debug(three_with_most)
        one, two, three = three_with_most[1], three_with_most[2], three_with_most[3]
        if elf > one:
            three_with_most.update({3: two, 2: one, 1: elf})
            continue
        if elf > two:
            three_with_most.update({3: two, 2: elf})
            continue
        if elf > three:
            three_with_most.update({3: elf})
            continue

    return sum(three_with_most.values())


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")


if __name__ == "__main__":
    main()
