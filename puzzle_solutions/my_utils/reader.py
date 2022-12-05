def get_puzzle_input(filename: str) -> list[str]:
    output = []
    with open(file=filename, mode='r') as f:
        for line in f:
            output.append(line.strip())
    return output
