from my_utils.reader import get_puzzle_input
from my_utils.logger import get_logger

INPUT_FILE = __file__.split(".")[0].replace("puzzle_solutions", "puzzle_input") + ".txt"
INPUT = get_puzzle_input(INPUT_FILE)
logger = get_logger()

class XList:
    x_list: list[int]
    
    def __init__(self) -> None:
        self.x_list = [1]
        
    def noop(self):
        self.x_list.append(self.x_list[-1])
        
    def add_x(self, x: int):
        self.x_list.append(self.x_list[-1])
        self.x_list.append(self.x_list[-1] + x)  
        
    def read_signal(self, instruction: str):
        if instruction == "noop":
            self.noop()
        else:
            self.add_x(int(instruction.split()[1]))
            
    def get_output(self, number: int) -> int:
        return self.x_list[number]

def part_1():
    output = XList()
    for line in INPUT:
        output.read_signal(line)
    strengths = []
    for i in range(20, len(output.x_list), 40):
        strengths.append(output.get_output(i))
    return sum(strengths)
        

def part_2():
    # TODO Replace with solution
    pass


def main() -> None:
    print(f"The answer to part 1 is {part_1()}")
    print(f"The answer to part 2 is {part_2()}")

if __name__ == "__main__":
    main()