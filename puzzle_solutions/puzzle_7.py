from dataclasses import dataclass
from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()
MAX_SIZE = 100000
REQUIRED_SPACE = 8381165


@dataclass
class File:
    name: str
    size: int
    parent: "Directory"


class Directory:
    name: str
    directories: list["SubDirectory"]
    files: list[File]
    size: int

    def __init__(self, name: str) -> None:
        self.name = name
        self.directories: list["SubDirectory"] = list()
        self.files = list()
        self.size = 0

    def add_entry(self, entry: str) -> None:
        if entry.startswith("dir "):
            self.directories.append(SubDirectory(entry.split()[1], self))
        else:
            self.files.append(File(entry.split()[1], int(entry.split()[0]), self))

    def change_dir(self, parameter: str) -> "Directory":
        return [
            directory for directory in self.directories if directory.name == parameter
        ][0]

    def calculate_size(self) -> None:
        size = 0
        for file in self.files:
            size += file.size
        for dir in self.directories:
            size += dir.get_size()
        self.size = size

    def get_size(self) -> int:
        if not self.size:
            self.calculate_size()
        return self.size


class SubDirectory(Directory):
    parent: "Directory"

    def __init__(self, name: str, parent: Directory) -> None:
        super().__init__(name)
        self.parent = parent

    def change_dir(self, command: str) -> "Directory":
        if command == "..":
            return self.parent
        else:
            return super().change_dir(command)


root = Directory("/")
all_directories: set[Directory] = set()


def change_dir(cwd: Directory, parameter: str) -> Directory:
    if parameter == "/":
        return root
    else:
        return cwd.change_dir(parameter)


def part_1():
    cwd = root
    all_directories.add(cwd)
    for line in INPUT:
        if line.startswith("$") and line.split()[1] == "cd":
            cwd = change_dir(cwd, line.split()[2])
            all_directories.add(cwd)
        if line.startswith("$"):
            continue
        else:
            cwd.add_entry(line)

    root.get_size()
    below_limit_dirs: list[Directory] = []
    for dir in all_directories:
        if dir.get_size() < MAX_SIZE:
            below_limit_dirs.append(dir)
    (below_limit_dirs.append(dir) for dir in all_directories if dir.size < MAX_SIZE)
    return sum([dir.size for dir in below_limit_dirs])


def part_2() -> int:
    current_lowest: Directory = root
    for dir in all_directories:
        if (
            dir.get_size() > REQUIRED_SPACE
            and dir.get_size() < current_lowest.get_size()
        ):
            current_lowest = dir

    return current_lowest.get_size()


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")


if __name__ == "__main__":
    main()
