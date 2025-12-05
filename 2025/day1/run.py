from typing import List
from solution import BaseSolution


class Solution(BaseSolution):

    def init(self) -> None:
        self.turns: List[tuple[str, int]] = []
        with open(self.filename, "r") as f:
            self.turns = [(turn[0], int(turn[1:])) for turn in f.readlines()]

    def stage1(self) -> int:
        dial, zeros = 50, 0
        for direction, clicks in self.turns:
            dial += clicks if direction == "R" else -clicks
            dial %= 100
            if dial == 0:
                zeros += 1
        return zeros

    def stage2(self) -> int:
        dial, zeros = 50, 0
        for direction, clicks in self.turns:
            for _ in range(clicks):
                dial += 1 if direction == "R" else -1
                dial %= 100
                if dial == 0:
                    zeros += 1
        return zeros


if __name__ == "__main__":
    Solution.main()
