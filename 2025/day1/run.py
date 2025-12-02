from typing import List

INPUT_FILE = "./input.txt"


def load_input() -> List[tuple[str, int]]:
    with open(INPUT_FILE, "r") as f:
        turns = [(turn[0], int(turn[1:])) for turn in f.readlines()]

    return turns


def stage1(turns: List[tuple[str, int]]) -> None:
    dial, zeros = 50, 0
    for direction, clicks in turns:
        dial += clicks if direction == "R" else -clicks
        dial %= 100
        if dial == 0:
            zeros += 1
    print("Zeros:", zeros)


def stage2(turns: List[tuple[str, int]]) -> None:
    dial, zeros = 50, 0
    for direction, clicks in turns:
        for _ in range(clicks):
            dial += 1 if direction == "R" else -1
            dial %= 100
            if dial == 0:
                zeros += 1
    print("Zeros:", zeros)


def main() -> None:
    turns = load_input()

    stage1(turns)
    stage2(turns)


if __name__ == "__main__":
    main()
