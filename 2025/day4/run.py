from typing import List

INPUT_FILE = "./input.txt"
EXAMPLE_FILE = "./example.txt"


def load_input() -> List[List[bool]]:
    map: List[List[bool]] = []
    with open(INPUT_FILE, "r") as f:
        for row in f.readlines():
            map.append([c == "@" for c in row.strip()])
    return map


def stage1(map: List[List[bool]]) -> int:
    def is_accessible(row, col) -> bool:
        tally = 0
        has_top = row > 0
        has_left = col > 0
        has_bottom = row < len(map) - 1
        has_right = col < len(map[0]) - 1

        if has_top and has_left and map[row - 1][col - 1]:
            tally += 1
        if has_top and map[row - 1][col]:
            tally += 1
        if has_top and has_right and map[row - 1][col + 1]:
            tally += 1
        if has_right and map[row][col + 1]:
            tally += 1
        if has_right and has_bottom and map[row + 1][col + 1]:
            tally += 1
        if has_bottom and map[row + 1][col]:
            tally += 1
        if has_bottom and has_left and map[row + 1][col - 1]:
            tally += 1
        if has_left and map[row][col - 1]:
            tally += 1

        return tally < 4

    accessible = 0
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] and is_accessible(row, col):
                accessible += 1

    return accessible


def stage2(map: List[List[bool]]) -> int:
    def is_accessible(row, col) -> bool:
        tally = 0
        has_top = row > 0
        has_left = col > 0
        has_bottom = row < len(map) - 1
        has_right = col < len(map[0]) - 1

        if has_top and has_left and map[row - 1][col - 1]:
            tally += 1
        if has_top and map[row - 1][col]:
            tally += 1
        if has_top and has_right and map[row - 1][col + 1]:
            tally += 1
        if has_right and map[row][col + 1]:
            tally += 1
        if has_right and has_bottom and map[row + 1][col + 1]:
            tally += 1
        if has_bottom and map[row + 1][col]:
            tally += 1
        if has_bottom and has_left and map[row + 1][col - 1]:
            tally += 1
        if has_left and map[row][col - 1]:
            tally += 1

        return tally < 4

    removed = 0
    while True:
        recent_removal = False
        for row in range(len(map)):
            for col in range(len(map[0])):
                if map[row][col] and is_accessible(row, col):
                    map[row][col] = False
                    recent_removal = True
                    removed += 1
        
        if not recent_removal:
            break

    return removed


def main() -> None:
    input = load_input()

    print("Stage 1:", stage1(input))
    print("Stage 2:", stage2(input))


if __name__ == "__main__":
    main()
