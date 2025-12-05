from typing import List


class Solution:
    INPUT_FILE = "./input.txt"
    EXAMPLE_FILE = "./example.txt"

    def __init__(self) -> None:
        self.fresh_ranges: List[List[int]] = []
        self.ingredients: List[int] = []
        with open(self.INPUT_FILE, "r") as f:
            for line in f.readlines():
                line = line.strip()
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


def main() -> None:
    s = Solution()

    print("Stage 1:", s.stage1())
    print("Stage 2:", s.stage2())


if __name__ == "__main__":
    main()
