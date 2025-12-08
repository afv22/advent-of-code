from aoc.base_solution import BaseSolution
from aoc.data_structures.matrix import VECTORS_8
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.map = IO.load_matrix(self.filename, lambda c: c == "@")

    def _is_accessible(self, row, col) -> bool:
        tally = 0
        for row_delta, col_delta in VECTORS_8:
            new_row, new_col = row + row_delta, col + col_delta
            if self.map.is_valid(new_row, new_col) and self.map[new_row][new_col]:
                tally += 1

        return tally < 4

    def stage1(self) -> int:
        accessible = 0
        for row in range(self.map.n_rows):
            for col in range(self.map.n_cols):
                if self.map[row][col] and self._is_accessible(row, col):
                    accessible += 1

        return accessible

    def stage2(self) -> int:
        removed = 0
        while True:
            recent_removal = False
            for row in range(self.map.n_rows):
                for col in range(self.map.n_cols):
                    if self.map[row][col] and self._is_accessible(row, col):
                        self.map[row][col] = False
                        recent_removal = True
                        removed += 1

            if not recent_removal:
                break

        return removed


if __name__ == "__main__":
    Solution.main()
