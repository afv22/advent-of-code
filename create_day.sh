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
from typing import List


class Solution:
    INPUT_FILE = "./input.txt"
    EXAMPLE_FILE = "./example.txt"

    def __init__(self) -> None:
        self.lines: List = []
        with open(self.EXAMPLE_FILE, "r") as f:
            for line in f.readlines():
                self.lines.append(line)

    def stage1(self) -> int: ...

    def stage2(self) -> int: ...


def main() -> None:
    s = Solution()

    print("Stage 1:", s.stage1())
    print("Stage 2:", s.stage2())


if __name__ == "__main__":
    main()
EOF

# Open challenge page
open https://adventofcode.com/$year/day/$day