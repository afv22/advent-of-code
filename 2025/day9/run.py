from itertools import combinations

from aoc.base_solution import BaseSolution
from aoc.data_structures import CompressedMatrix


class Solution(BaseSolution):

    def init(self) -> None:
        pairs = [line.split(",") for line in self.load_lines()]
        self.tiles = [(int(row), int(col)) for col, row in pairs]
        self.matrix = CompressedMatrix(self.tiles)

    def stage1(self) -> int:
        largest_area = -1
        for (r1, c1), (r2, c2) in combinations(self.tiles, 2):
            area = (1 + abs(r1 - r2)) * (1 + abs(c1 - c2))
            largest_area = max(largest_area, area)
        return largest_area

    def _valid_rectangle(self, tile1, tile2):
        (r1, c1), (r2, c2) = tile1, tile2
        min_r, max_r = min(r1, r2), max(r1, r2)
        min_c, max_c = min(c1, c2), max(c1, c2)
        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                if self.matrix[r][c] == " ":
                    return False
        return True

    def stage2(self) -> int:
        # Mark all tiles
        ctiles = self.matrix.compress_list(self.tiles)
        for i in range(len(ctiles) - 1):
            self.matrix.fill_range(ctiles[i], ctiles[i + 1], "X")
        self.matrix.fill_range(ctiles[0], ctiles[-1], "X")
        self.matrix.flood((57, 125), "X")

        # Calculate rectangles areas
        rectangles = []
        for (r1, c1), (r2, c2) in combinations(self.tiles, 2):
            area = (1 + abs(r1 - r2)) * (1 + abs(c1 - c2))
            cr1, cc1 = self.matrix.compress((r1, c1))
            cr2, cc2 = self.matrix.compress((r2, c2))
            rectangles.append((area, (cr1, cc1), (cr2, cc2)))

        # Find largest valid rectangle
        for area, point1, point2 in sorted(rectangles, reverse=True):
            if self._valid_rectangle(point1, point2):
                return area
        return -1


if __name__ == "__main__":
    Solution.main()
