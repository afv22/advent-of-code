from typing import List

from aoc.base_solution import BaseSolution
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.equations: List[tuple[int, List[int]]] = []
        for line in IO.load_lines(self.filename):
            target, raw_values = line.split(":")
            values = map(int, raw_values.strip().split())
            self.equations.append((int(target), list(values)))

    @classmethod
    def _check_values(cls, target: int, values: List[int], allow_concat: bool) -> bool:
        def fn(tally, values):
            if not values:
                return target == tally

            value, values = values[0], values[1:]
            if fn(tally + value, values):
                return True

            if fn(tally * value, values):
                return True

            if allow_concat and fn(int(str(tally) + str(value)), values):
                return True

            return False

        return fn(0, values)

    def stage1(self) -> int:
        total = 0
        for target, values in self.equations:
            if self._check_values(target, values, False):
                total += target
        return total

    def stage2(self) -> int:
        total = 0
        for target, values in self.equations:
            if self._check_values(target, values, True):
                total += target
        return total


if __name__ == "__main__":
    Solution.main()
