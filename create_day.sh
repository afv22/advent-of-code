#!/bin/bash

source .env

year=$1
day=$2

# Create files
mkdir -p "$year/day$day"
touch "$year/day$day/input.txt"
touch "$year/day$day/example.txt"

# Fetch challenge input
curl -b "session=$AOC_COOKIE" https://adventofcode.com/$year/day/$day/input > "$year/day$day/input.txt"

# Generate boilerplate script
cat > "$year/day$day/run.py" << 'EOF'
INPUT_FILE = "./input.txt"
EXAMPLE_FILE = "./example.txt"


def load_input() -> str:
    with open(INPUT_FILE, "r") as f:
        s = f.read()

    return s


def stage1(input) -> int:
    return -1


def stage2(input) -> int:
    return -1


def main() -> None:
    input = load_input()

    print("Stage 1:", stage1(input))
    print("Stage 2:", stage2(input))


if __name__ == "__main__":
    main()
EOF

# Open challenge page
open https://adventofcode.com/$year/day/$day