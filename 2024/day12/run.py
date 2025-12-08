from aoc.base_solution import BaseSolution
from aoc.data_structures.matrix import VECTORS_4, VECTORS_DIAG
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.garden = IO.load_matrix(self.filename)

    def _is_inside_region(self, row: int, col: int, region: str):
        return self.garden.is_valid(row, col) and self.garden[row][col] == region

    def _map_region(self, start_row: int, start_col: int):
        """Returns set of all cells in the region starting from (start_row, start_col)."""
        cells = set()
        region = self.garden[start_row][start_col]
        to_explore = [(start_row, start_col)]

        while to_explore:
            row, col = to_explore.pop()
            if (row, col) in cells:
                continue

            cells.add((row, col))
            for dr, dc in VECTORS_4:
                new_row, new_col = row + dr, col + dc
                if self._is_inside_region(new_row, new_col, region):
                    to_explore.append((new_row, new_col))

        return cells

    def _count_corners(self, row: int, col: int):
        """Count corners for a single cell."""
        region = self.garden[row][col]
        corners = 0
        for dr, dc in VECTORS_DIAG:
            side1 = self._is_inside_region(row + dr, col, region)
            side2 = self._is_inside_region(row, col + dc, region)
            diag = self._is_inside_region(row + dr, col + dc, region)

            # Convex: both sides outside
            if not side1 and not side2:
                corners += 1
            # Concave: both sides inside, diagonal outside
            elif side1 and side2 and not diag:
                corners += 1

        return corners

    def stage1(self) -> int:
        visited_global = set()
        price_total = 0

        for row, col in self.garden.coordinates:
            if (row, col) in visited_global:
                continue

            region = self.garden[row][col]
            cells = self._map_region(row, col)
            visited_global.update(cells)

            # Calculate perimeter
            perimeter = 0
            for r, c in cells:
                for dr, dc in VECTORS_4:
                    if not self._is_inside_region(r + dr, c + dc, region):
                        perimeter += 1

            price_total += len(cells) * perimeter

        return price_total

    def stage2(self) -> int:
        visited_global = set()
        price_total = 0

        for row, col in self.garden.coordinates:
            if (row, col) in visited_global:
                continue

            cells = self._map_region(row, col)
            visited_global.update(cells)
            sides = sum(self._count_corners(r, c) for r, c in cells)
            price_total += len(cells) * sides

        return price_total


if __name__ == "__main__":
    Solution.main()
