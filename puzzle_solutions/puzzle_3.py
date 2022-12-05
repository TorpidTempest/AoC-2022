import string
from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()

def get_priority(character: str) -> int:
    if character in string.ascii_lowercase:
        return ord(character) - 96
    if character in string.ascii_uppercase:
        return ord(character) - 38
    return 0
        

def part_1() -> int:
    letters: list[str] = []
    for line in INPUT:
        midpoint = len(line) // 2
        one, two = line[:midpoint], line[midpoint:]
        for letter in one:
            if letter in two:
                letters.append(letter)
                break
    result = 0
    for letter in letters:
        result += get_priority(letter)
    
    return result

def part_2():
    badges: list[str] = []
    for i in range(0, len(INPUT), 3):
        intersection = set(INPUT[i]).intersection(INPUT[i+1]).intersection(INPUT[i+2])
        badges.append(intersection.pop())
    result = sum([get_priority(badge) for badge in badges])
    return result
        


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")

if __name__ == "__main__":
    main()