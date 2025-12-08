from typing import List

from aoc.base_solution import BaseSolution
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.map: List[List[bool]] = []
        for row in IO.load_lines(self.filename):
            self.map.append([c == "@" for c in row])

    def _is_accessible(self, row, col) -> bool:
        tally = 0
        has_top = row > 0
        has_left = col > 0
        has_bottom = row < len(self.map) - 1
        has_right = col < len(self.map[0]) - 1

        if has_top and has_left and self.map[row - 1][col - 1]:
            tally += 1
        if has_top and self.map[row - 1][col]:
            tally += 1
        if has_top and has_right and self.map[row - 1][col + 1]:
            tally += 1
        if has_right and self.map[row][col + 1]:
            tally += 1
        if has_right and has_bottom and self.map[row + 1][col + 1]:
            tally += 1
        if has_bottom and self.map[row + 1][col]:
            tally += 1
        if has_bottom and has_left and self.map[row + 1][col - 1]:
            tally += 1
        if has_left and self.map[row][col - 1]:
            tally += 1

        return tally < 4

    def stage1(self) -> int:
        accessible = 0
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if self.map[row][col] and self._is_accessible(row, col):
                    accessible += 1

        return accessible

    def stage2(self) -> int:
        removed = 0
        while True:
            recent_removal = False
            for row in range(len(self.map)):
                for col in range(len(self.map[0])):
                    if self.map[row][col] and self._is_accessible(row, col):
                        self.map[row][col] = False
                        recent_removal = True
                        removed += 1

            if not recent_removal:
                break

        return removed


if __name__ == "__main__":
    Solution.main()
