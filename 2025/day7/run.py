from collections import defaultdict

from aoc.base_solution import BaseSolution


class Solution(BaseSolution):

    def init(self) -> None:
        self.lines = self.load_lines()

    def stage1(self) -> int:
        beams = set([self.lines[0].index("S")])
        splits = 0
        for line in self.lines[1:]:
            for i, c in enumerate(line):
                if c == "^" and i in beams:
                    beams.remove(i)
                    beams.add(i - 1)
                    beams.add(i + 1)
                    splits += 1

        return splits

    def stage2(self) -> int:
        beams = defaultdict(lambda: 0)
        beams[self.lines[0].index("S")] = 1
        for line in self.lines[1:]:
            for i, c in enumerate(line):
                if c == "^" and i in beams:
                    beams[i - 1] += beams[i]
                    beams[i + 1] += beams[i]
                    del beams[i]

        return sum(beams.values())


if __name__ == "__main__":
    Solution.main()
