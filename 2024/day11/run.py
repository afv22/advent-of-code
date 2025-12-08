from collections import defaultdict
from typing import Dict, List

from aoc.base_solution import BaseSolution
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.stones = [int(n) for n in IO.load_raw(self.filename).split()]

    def _process_stone(self, stone: int) -> List[int]:
        if not stone:
            return [1]

        stone_string = str(stone)
        if len(stone_string) % 2:
            return [stone * 2024]

        mid = len(stone_string) // 2
        left, right = stone_string[:mid], stone_string[mid:]
        return [int(left), int(right)]

    def stage1(self) -> int:
        stones = self.stones
        for _ in range(25):
            new_stones = []
            for stone in stones:
                new_stones += self._process_stone(stone)
            stones = new_stones
        return len(stones)

    def stage2(self) -> int:
        stones = defaultdict(lambda: 0)
        for stone in self.stones:
            stones[stone] += 1

        for _ in range(75):
            new_stones = defaultdict(lambda: 0)
            for stone in stones:
                processed_stones = self._process_stone(stone)
                for pstone in processed_stones:
                    new_stones[pstone] += stones[stone]

            stones = new_stones

        return sum(stones.values())


if __name__ == "__main__":
    Solution.main()
