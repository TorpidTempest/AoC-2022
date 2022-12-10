from enum import Enum
from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger
from dataclasses import dataclass

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()


class Direction:
    LEFT = "L"
    DOWN = "D"
    UP = "U"
    RIGHT = "R"


@dataclass
class Knot:
    x_pos: int
    y_pos: int

    def chase_knot(self, knot: "Knot"):
        x_diff = knot.x_pos - self.x_pos
        y_diff = knot.y_pos - self.y_pos

        if abs(x_diff) <= 1 and abs(y_diff) <= 1:  # No move needed
            pass
        elif abs(x_diff) > 1:
            self.x_pos += 1 if x_diff > 1 else -1
            self.y_pos += y_diff
        else:
            self.y_pos += 1 if y_diff > 1 else -1
            self.x_pos += x_diff
            


class Rope:
    head: Knot
    tail: Knot
    tail_trail: set[tuple[int, int]]

    def __init__(self) -> None:
        self.head = Knot(0, 0)
        self.tail = Knot(0, 0)
        self.tail_trail = set()
        self.tail_trail.add((0, 0))

    def __repr__(self) -> str:
        return f"Head - {self.head} \n" + f"Tail - {self.tail}"

    def move_head(self, direction: str):
        match direction:
            case Direction.UP:
                self.head.y_pos += 1
            case Direction.DOWN:
                self.head.y_pos -= 1
            case Direction.LEFT:
                self.head.x_pos -= 1
            case Direction.RIGHT:
                self.head.x_pos += 1

    def chase_tail(self, direction: str):
        if (  # No move needed
            abs(self.head.x_pos - self.tail.x_pos) <= 1
            and abs(self.head.y_pos - self.tail.y_pos) <= 1
        ):
            pass

        elif (  # Straight up or down
            self.head.x_pos == self.tail.x_pos
            and abs(self.head.y_pos - self.tail.y_pos) > 1
        ):
            self.tail.y_pos += 1 if direction == Direction.UP else -1

        elif (  # Straight left or right
            self.head.y_pos == self.tail.y_pos
            and abs(self.head.x_pos - self.tail.x_pos) > 1
        ):
            self.tail.x_pos += 1 if direction == Direction.RIGHT else -1

        elif direction in (Direction.LEFT, Direction.RIGHT):
            self.tail.y_pos = self.head.y_pos
            self.tail.x_pos += 1 if direction == Direction.RIGHT else -1

        else:
            self.tail.x_pos = self.head.x_pos
            self.tail.y_pos += 1 if direction == Direction.UP else -1

    def move(self, direction: str, moves: int):
        for _ in range(moves):
            self.move_head(direction)
            self.chase_tail(direction)
            self.tail_trail.add((self.tail.x_pos, self.tail.y_pos))


class Rope2:
    knots: list[Knot]
    tail_trail: set[tuple[int, int]]

    def __init__(self, length: int) -> None:
        self.knots = [Knot(0, 0) for _ in range(length)]
        self.tail_trail = set()
        self.tail_trail.add((0, 0))
        
    def __repr__(self) -> str:
        return str(self.knots)

    def move_head(self, direction: str):
        match direction:
            case Direction.UP:
                self.knots[0].y_pos += 1
            case Direction.DOWN:
                self.knots[0].y_pos -= 1
            case Direction.LEFT:
                self.knots[0].x_pos -= 1
            case Direction.RIGHT:
                self.knots[0].x_pos += 1


    def move(self, direction: str, moves: int):
        for _ in range(moves):
            self.move_head(direction)
            for i, _ in enumerate(self.knots[1:]):
                self.knots[i+1].chase_knot(self.knots[i])
            self.tail_trail.add((self.knots[-1].x_pos, self.knots[-1].y_pos))


def part_1():
    rope = Rope()
    for instruction in INPUT:
        rope.move(instruction.split()[0], int(instruction.split()[1]))
    return len(rope.tail_trail)


def part_2():
    rope = Rope2(10)
    for instruction in INPUT:
        rope.move(instruction.split()[0], int(instruction.split()[1]))
    return len(rope.tail_trail)


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")


if __name__ == "__main__":
    main()
