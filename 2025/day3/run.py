from solution import BaseSolution
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.banks = IO.load_lines(self.filename)

    def stage1(self) -> int:
        total = 0
        for bank in self.banks:
            l, r = bank[-2:]
            for n in bank[:-2][::-1]:
                if n >= l:
                    l, r = n, max(l, r)
            total += int(l + r)
        return total

    def stage2(self) -> int:
        def propagate(n: str, enabled: str) -> str:
            if not enabled or n < enabled[0]:
                return enabled
            return n + propagate(enabled[0], enabled[1:])

        total = 0
        for bank in self.banks:
            enabled = bank[-12:]
            for n in bank[:-12][::-1]:
                enabled = propagate(n, enabled)
            total += int(enabled)
        return total


if __name__ == "__main__":
    Solution.main()
