import argparse
from abc import ABC, abstractmethod


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

    @classmethod
    def main(cls) -> None:
        """Parse command-line arguments and run the solution."""
        parser = argparse.ArgumentParser(description="Run Advent of Code solution")
        parser.add_argument(
            "--real", action="store_true", help="Use input.txt instead of example.txt"
        )
        args = parser.parse_args()

        solution = cls(use_example=not args.real)

        print("Stage 1:", solution.stage1())
        print("Stage 2:", solution.stage2())
