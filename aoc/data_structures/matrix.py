from collections import deque
from typing import Iterator, List

# Right, Down, Left, Up
VECTORS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
VECTORS_8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
VECTORS_DIAG = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


class Matrix:
    def __init__(self, grid: List[List]) -> None:
        if not grid:
            raise ValueError("Matrix cannot be empty")

        self._grid = grid
        self.n_rows = len(self._grid)
        self.n_cols = len(self._grid[0])

    def __getitem__(self, index):
        return self._grid[index]

    def is_valid(self, row: int, col: int) -> bool:
        return 0 <= row < self.n_rows and 0 <= col < self.n_cols

    @property
    def rows(self) -> Iterator[List]:
        """Returns a generator that yields each row in the matrix."""
        for row in self._grid:
            yield row

    @property
    def cols(self) -> Iterator[List]:
        """Returns a generator that yields each column in the matrix."""
        for i in range(self.n_cols):
            yield [row[i] for row in self.rows]

    @property
    def coordinates(self) -> Iterator[tuple[int, int]]:
        """Returns a generator that yields each coordinate in the matrix."""
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                yield (r, c)

    def __str__(self) -> str:
        return "\n".join("".join(str(c) for c in row) for row in self.rows)

    def flood(self, starting_point: tuple[int, int], char: str | int) -> None:
        """Flood a section of the grid with a given character."""
        dq = deque([starting_point])
        while dq:
            row, col = dq.popleft()
            if self.is_valid(row, col) and self[row][col] != char:
                self[row][col] = char
                dq.append((row - 1, col))
                dq.append((row + 1, col))
                dq.append((row, col - 1))
                dq.append((row, col + 1))

    def fill_range(
        self, point1: tuple[int, int], point2: tuple[int, int], char: str | int
    ) -> None:
        (r1, c1), (r2, c2) = point1, point2
        min_r, max_r = min(r1, r2), max(r1, r2)
        min_c, max_c = min(c1, c2), max(c1, c2)
        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                if self[r][c] != char:
                    self[r][c] = char
