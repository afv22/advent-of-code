from typing import List

from .matrix import Matrix


class CompressedMatrix(Matrix):
    def __init__(self, points: List[tuple[int, int]]) -> None:
        unique_rows = sorted(set(r for r, _ in points))
        unique_cols = sorted(set(c for _, c in points))

        self.row_map = {orig: comp for comp, orig in enumerate(unique_rows)}
        self.col_map = {orig: comp for comp, orig in enumerate(unique_cols)}

        grid = [[" "] * len(unique_cols) for _ in range(len(unique_rows))]
        super().__init__(grid)

    def compress(self, point: tuple[int, int]) -> tuple[int, int]:
        """Convert original coordinates to compressed coordinates"""
        r, c = point
        return (self.row_map[r], self.col_map[c])

    def compress_list(self, points: List[tuple[int, int]]) -> List[tuple[int, int]]:
        """Compress a list of points"""
        return [self.compress(p) for p in points]
