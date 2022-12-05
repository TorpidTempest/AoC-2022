def get_puzzle_input(filename: str, stripped: bool = True) -> list[str]:
    output = []
    with open(file=filename, mode="r") as f:
        for line in f:
            output.append(line.strip() if stripped else line)
    return output
