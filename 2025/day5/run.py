from typing import List
from solution import BaseSolution
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.fresh_ranges: List[List[int]] = []
        self.ingredients: List[int] = []
        for line in IO.load_lines(self.filename):
            if "-" in line:
                low, high = line.split("-")
                self.fresh_ranges.append([int(low), int(high)])
            elif line:
                self.ingredients.append(int(line))

    def _clean_ranges(self) -> list[List[int]]:
        fresh_ranges = sorted(self.fresh_ranges, key=lambda tpl: tpl[0])
        clean_fresh_ranges = [fresh_ranges[0]]

        for low, high in fresh_ranges[1:]:
            if low <= clean_fresh_ranges[-1][1]:
                clean_fresh_ranges[-1][1] = max(clean_fresh_ranges[-1][1], high)
            else:
                clean_fresh_ranges.append([low, high])

        return clean_fresh_ranges

    def stage1(self) -> int:
        ranges = self._clean_ranges()
        fresh_ingredients = 0
        for ingr in self.ingredients:
            for low, high in ranges:
                if low <= ingr <= high:
                    fresh_ingredients += 1
                    break

        return fresh_ingredients

    def stage2(self) -> int:
        ranges = self._clean_ranges()
        return sum(high - low + 1 for low, high in ranges)


if __name__ == "__main__":
    Solution.main()
