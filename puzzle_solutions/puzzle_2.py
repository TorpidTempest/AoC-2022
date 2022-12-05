from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()

def part_1():
    score = 0
    WINS = {"A Y", "B Z", "C X"}
    DRAWS = {"A X", "B Y", "C Z"}
    for line in INPUT:
        pick = line.split()[1]
        match pick:
            case "X":
                score += 1
            case "Y":
                score += 2
            case "Z":
                score += 3
        if line in WINS:
            score += 6
            continue
        if line in DRAWS:
            score += 3
            
    return score


def part_2():
    pass


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")

if __name__ == "__main__":
    main()