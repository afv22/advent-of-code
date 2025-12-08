from typing import Iterator, List

VECTORS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
VECTORS_8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


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
