from aoc.base_solution import BaseSolution
from aoc.data_structures.matrix import VECTORS_8
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.grid = IO.load_matrix(self.filename)

    def stage1(self) -> int:
        tally = 0
        LETTERS = "MAS"
        for row, col in self.grid.coordinates:
            if self.grid[row][col] != "X":
                continue

            for delta_row, delta_col in VECTORS_8:
                new_row, new_col = row, col
                for char in LETTERS:
                    new_row += delta_row
                    new_col += delta_col
                    if (
                        not self.grid.is_valid(new_row, new_col)
                        or self.grid[new_row][new_col] != char
                    ):
                        break
                else:
                    tally += 1

        return tally

    def stage2(self) -> int:
        tally = 0
        LETTERS = "MS"
        for row, col in self.grid.coordinates:
            if not (0 < row < self.grid.n_rows - 1 and 0 < col < self.grid.n_cols - 1):
                continue

            if self.grid[row][col] != "A":
                continue

            top_left = self.grid[row - 1][col - 1]
            top_right = self.grid[row - 1][col + 1]
            bottom_right = self.grid[row + 1][col + 1]
            bottom_left = self.grid[row + 1][col - 1]
            if (
                top_left in LETTERS
                and bottom_right in LETTERS
                and top_left != bottom_right
                and top_right in LETTERS
                and bottom_left in LETTERS
                and top_right != bottom_left
            ):
                tally += 1

        return tally


if __name__ == "__main__":
    Solution.main()
