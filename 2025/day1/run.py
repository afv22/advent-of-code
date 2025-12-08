from aoc.base_solution import BaseSolution
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        lines = IO.load_lines(self.filename)
        self.turns = [(turn[0], int(turn[1:])) for turn in lines]

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
