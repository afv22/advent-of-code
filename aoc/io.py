from typing import List


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
