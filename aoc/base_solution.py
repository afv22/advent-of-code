import argparse
import sys
import threading
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Callable, List, Optional

from .data_structures import Matrix


class BaseSolution(ABC):
    INPUT_FILE = "./input.txt"
    EXAMPLE_FILE = "./example.txt"
    EXAMPLE_FILE_2 = None

    def __init__(self, use_example=True) -> None:
        self.use_example = use_example
        self._current_example_file = self.EXAMPLE_FILE
        self.init()
        super().__init__()

    @property
    def filename(self) -> str:
        return self._current_example_file if self.use_example else self.INPUT_FILE

    @abstractmethod
    def init(self) -> None: ...

    @abstractmethod
    def stage1(self) -> int: ...

    @abstractmethod
    def stage2(self) -> int: ...

    @staticmethod
    def _run_stage(stage: Callable, n: int, quiet: bool) -> None:
        start_time = time.time()

        # Flag to stop the timer thread
        stop_timer = threading.Event()

        def update_timer():
            if quiet:
                return

            while not stop_timer.is_set():
                elapsed = time.time() - start_time
                sys.stdout.write(f"\rStarting Stage {n}... ({elapsed:.2f}s)")
                sys.stdout.flush()
                time.sleep(0.01)  # Update every 10ms

        # Start timer thread
        print()  # New line before starting
        timer_thread = threading.Thread(target=update_timer, daemon=True)
        timer_thread.start()

        # Run the stage
        result = stage()

        # Stop the timer
        stop_timer.set()
        timer_thread.join()

        # Print final result
        duration = time.time() - start_time
        sys.stdout.write(f"\rStarting Stage {n}... ({duration:.2f}s)\n")
        print(f"Result: {result}")

    @classmethod
    def main(cls) -> None:
        """Parse command-line arguments and run the solution."""
        parser = argparse.ArgumentParser(description="Run Advent of Code solution")
        parser.add_argument(
            "--real", action="store_true", help="Use input.txt instead of example.txt"
        )
        parser.add_argument("--quiet", action="store_true", help="Suppress runtime")
        args = parser.parse_args()

        solution = cls(use_example=not args.real)

        year, day = Path.cwd().parts[-2:]
        print(f"Starting execution for Day {day[3:]}, {year}...")
        cls._run_stage(solution.stage1, 1, args.quiet)

        # Switch to second example file for stage 2 if configured
        if solution.use_example and cls.EXAMPLE_FILE_2 is not None:
            solution._current_example_file = cls.EXAMPLE_FILE_2
            solution.init()

        cls._run_stage(solution.stage2, 2, args.quiet)
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
