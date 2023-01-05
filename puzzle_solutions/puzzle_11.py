from collections import deque
from dataclasses import dataclass
from math import floor
from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()


@dataclass
class Monkey:
    name: str
    items: deque[int]
    operation: str
    test: int
    if_true: int
    if_false: int
    inspections: int = 0

    def monkey_business(self) -> tuple[int, int]:
        item = self.items.pop()
        op = self.operation.split()
        match op[3]:
            case "+":
                item += int(op[-1]) if op[-1].isdigit() else item
            case "*":
                item *= int(op[-1]) if op[-1].isdigit() else item
            case "-":
                item -= int(op[-1]) if op[-1].isdigit() else item
            case "/":
                item /= int(op[-1]) if op[-1].isdigit() else item
            case _:
                logger.error("no match")
        item //= 3

        passed_to = self.if_true if item % self.test == 0 else self.if_false
        worry = floor(item)
        self.inspections += 1

        return worry, passed_to
    
    def get_item(self, item: int):
        self.items.append(item)
        
    def give_item(self, item: int, monkey:"Monkey"):
        pass


def generate_monkey(monkey_stats: list[str]) -> Monkey:
    name = monkey_stats[0][:-1]
    items: list[int] = [
        int(item) for item in monkey_stats[1].split(":")[1].split(",")
    ]
    operation = monkey_stats[2].split(":")[1]
    test = int(monkey_stats[3].split()[-1])
    if_true = int(monkey_stats[4].split()[-1])
    if_false = int(monkey_stats[5].split()[-1])
    monkey = Monkey(name, deque(items), operation, test, if_true, if_false)
    return monkey


def part_1(monkeys: list[Monkey]):
    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                worry, passed_to = monkey.monkey_business()
                monkeys[passed_to].get_item(worry)
    for monkey in monkeys:
        logger.info(monkey.inspections)
    # NOT WORKING CURRENTLY
    first: int = 0
    second: int = 0
    for monkey in monkeys:
        if monkey.inspections > monkeys[first].inspections:
            first, second = int(monkey.name.split()[-1]), monkeys[first].inspections
        elif monkey.inspections > monkeys[second].inspections:
            second = int(monkey.name.split()[-1])
            

            
    return monkeys[first].inspections + monkeys[second].inspections

def part_2():
    # TODO Replace with solution
    pass


def main() -> None:
    monkeys: list[Monkey] = []
    for i, line in enumerate(INPUT):
        if line.startswith("Monkey"):
            monkeys.append(generate_monkey(INPUT[i : i + 6]))


    print(f"The answer to part 1 is {part_1(monkeys)}")
    print(f"The answer to part 2 is {part_2()}")


if __name__ == "__main__":
    main()
