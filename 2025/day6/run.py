from functools import reduce

from aoc.base_solution import BaseSolution
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.lines = IO.load_lines(self.filename)
        self.grid = IO.load_matrix(self.filename)

    def stage1(self) -> int:
        lines = [line.split() for line in self.lines]

        total = 0
        for i in range(len(lines[0])):
            op = lines[-1][i]
            vals = [int(line[i]) for line in lines[:-1]]
            if op == "+":
                total += sum(vals)
            elif op == "*":
                total += reduce(lambda x, y: x * y, vals)

        return total

    def stage2(self) -> int:
        total = 0
        curr_vals = []
        curr_op = None

        def new_total() -> int:
            if curr_op == "+":
                return total + sum(curr_vals)
            elif curr_op == "*":
                return total + reduce(lambda x, y: x * y, curr_vals)
            return 0

        for column in self.grid.cols:
            if all(c == " " for c in column):
                total = new_total()
                curr_vals = []
                curr_op = None
            else:
                if column[-1] != " ":
                    curr_op = column[-1]
                curr_vals.append(int("".join(column[:-1])))

        total = new_total()
        return total


if __name__ == "__main__":
    Solution.main()
