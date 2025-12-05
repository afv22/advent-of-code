from typing import List
from solution import BaseSolution


class Solution(BaseSolution):

    def init(self) -> None:
        self.ranges: List[tuple[int, int]] = []
        with open(self.filename, "r") as f:
            s = f.read().strip()

        raw_ranges = s.split(",")
        for rr in raw_ranges:
            low, high = rr.split("-")
            self.ranges.append((int(low), int(high)))

    def stage1(self) -> int:
        total = 0
        for low, high in self.ranges:
            for n in range(low, high + 1):
                s = str(n)
                if len(s) % 2 == 0:
                    mid = len(s) // 2
                    if s[:mid] == s[mid:]:
                        total += n

        return total

    def stage2(self) -> int:
        total = 0
        # For each range
        for low, high in self.ranges:
            # For each number in that range
            for n in range(low, high + 1):
                s = str(n)
                # For each chunk in that number
                for chunk_size in range(1, (len(s) // 2) + 1):
                    if len(s) % chunk_size == 0:
                        # Check for repeating pattern
                        pattern = s[:chunk_size]
                        if pattern * (len(s) // chunk_size) == s:
                            total += n
                            break

        return total


if __name__ == "__main__":
    Solution.main()
