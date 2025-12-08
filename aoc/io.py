from typing import Any, Callable, List, Optional
from .data_structures import Matrix


class IO:
    @staticmethod
    def load_lines(filename: str) -> List[str]:
        lines: List[str] = []
        with open(filename, "r") as f:
            for line in f.readlines():
                line = line.strip("\n")
                lines.append(line)
        return lines

    @staticmethod
    def load_raw(filename: str) -> str:
        with open(filename, "r") as f:
            return f.read().strip("\n")

    @staticmethod
    def load_matrix(
        filename: str, func: Optional[Callable[[str], Any]] = None
    ) -> Matrix:
        grid = []
        with open(filename, "r") as f:
            for line in f.readlines():
                line = line.strip("\n")
                if func:
                    grid.append([func(c) for c in line])
                else:
                    grid.append(list(line))
        return Matrix(grid)
