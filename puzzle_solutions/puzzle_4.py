from dataclasses import dataclass
from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()


@dataclass
class Elf:
    start: int
    end: int

    def check_containment(self, other: "Elf") -> bool:
        if self.start >= other.start and self.end <= other.end:
            return True
        if self.start <= other.start and self.end >= other.end:
            return True
        return False

    def check_overlap(self, other: "Elf") -> bool:
        if self.start > other.end:
            return False
        if self.end < other.start:
            return False
        return True


def part_1():
    contains = 0
    for line in INPUT:
        elf_1_str, elf_2_str = line.split(",")[0], line.split(",")[1]
        elf_1: Elf = Elf(int(elf_1_str.split("-")[0]), int(elf_1_str.split("-")[1]))
        elf_2: Elf = Elf(int(elf_2_str.split("-")[0]), int(elf_2_str.split("-")[1]))
        if elf_1.check_containment(elf_2):
            contains += 1
    return contains


def part_2():
    overlaps = 0
    for line in INPUT:
        elf_1_str, elf_2_str = line.split(",")[0], line.split(",")[1]
        elf_1: Elf = Elf(int(elf_1_str.split("-")[0]), int(elf_1_str.split("-")[1]))
        elf_2: Elf = Elf(int(elf_2_str.split("-")[0]), int(elf_2_str.split("-")[1]))
        if elf_1.check_overlap(elf_2):
            overlaps += 1
    return overlaps


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")


if __name__ == "__main__":
    main()
