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
from solution import BaseSolution


class Solution(BaseSolution):

    def init(self) -> None:
        self.lines: List = []
        with open(self.filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                self.lines.append(line)

    def stage1(self) -> int: ...
    def stage2(self) -> int: ...


if __name__ == "__main__":
    Solution.main()
EOF

# Open challenge page
open https://adventofcode.com/$year/day/$day
