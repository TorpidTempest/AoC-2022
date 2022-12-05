from collections import deque
from dataclasses import dataclass
from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE, stripped=False)
logger = get_logger()


@dataclass
class Instruction:
    moves: int
    start: int
    finish: int


# * Hard coding the stacks because i'm lazy, would refine later if I didn't
# * inevitably get distracted by something else
def get_stacks() -> list[deque[str]]:
    stacks: list[deque[str]] = [deque() for _ in range(9)]
    for stack_num, stack in enumerate(stacks):
        for i in range(7, -1, -1):
            crate = INPUT[i][stack_num * 4 + 1]
            if crate != " ":
                stack.append(crate)

    return stacks


def get_instructions() -> list[Instruction]:
    instructions: list[Instruction] = []
    for i in range(10, len(INPUT)):
        line_decomp = INPUT[i].split()
        instructions.append(
            Instruction(int(line_decomp[1]), int(line_decomp[3]), int(line_decomp[5]))
        )

    return instructions


def part_1() -> str:
    stacks = get_stacks()
    instructions = get_instructions()
    
    for instruction in instructions:
        for _ in range(instruction.moves):
            stacks[instruction.finish-1].append(stacks[instruction.start-1].pop())

    return "".join(stack.pop() for stack in stacks)


def part_2():
    stacks = get_stacks()
    instructions = get_instructions()
    crane: deque[str] = deque()
    for instruction in instructions:
        for _ in range(instruction.moves):
            crane.append(stacks[instruction.start-1].pop())
        for _ in range(instruction.moves):
            stacks[instruction.finish-1].append(crane.pop())
    
    return "".join(stack.pop() for stack in stacks)
        


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")


if __name__ == "__main__":
    main()
