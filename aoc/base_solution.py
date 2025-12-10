import argparse
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Callable, List, Optional

from .data_structures import Matrix


class BaseSolution(ABC):
    INPUT_FILE = "./input.txt"
    EXAMPLE_FILE = "./example.txt"

    def __init__(self, use_example=True) -> None:
        self.use_example = use_example
        self.init()
        super().__init__()

    @property
    def filename(self) -> str:
        return self.EXAMPLE_FILE if self.use_example else self.INPUT_FILE

    @abstractmethod
    def init(self) -> None: ...

    @abstractmethod
    def stage1(self) -> int: ...

    @abstractmethod
    def stage2(self) -> int: ...

    @staticmethod
    def _run_stage(stage: Callable, n: int) -> None:
        print(f"\nStarting Stage {n}...")

        start_time = time.time()
        result = stage()
        duration = time.time() - start_time

        print(f"Result: {result}\t({duration:.2f}s)")

    @classmethod
    def main(cls) -> None:
        """Parse command-line arguments and run the solution."""
        parser = argparse.ArgumentParser(description="Run Advent of Code solution")
        parser.add_argument(
            "--real", action="store_true", help="Use input.txt instead of example.txt"
        )
        args = parser.parse_args()

        solution = cls(use_example=not args.real)

        year, day = Path.cwd().parts[-2:]
        print(f"Starting execution for Day {day[3:]}, {year}...")
        cls._run_stage(solution.stage1, 1)
        cls._run_stage(solution.stage2, 2)
        print()

    def load_lines(self) -> List[str]:
        lines: List[str] = []
        with open(self.filename, "r") as f:
            for line in f.readlines():
                line = line.strip("\n")
                lines.append(line)
        return lines

    def load_raw(self) -> str:
        with open(self.filename, "r") as f:
            return f.read().strip("\n")

    def load_matrix(self, func: Optional[Callable[[str], Any]] = None) -> Matrix:
        grid = []
        with open(self.filename, "r") as f:
            for line in f.readlines():
                line = line.strip("\n")
                if func:
                    grid.append([func(c) for c in line])
                else:
                    grid.append(list(line))
        return Matrix(grid)
