import heapq
from collections import namedtuple
from typing import List

from aoc.base_solution import BaseSolution
from aoc.io import IO

Machine = namedtuple("Machine", ["buttonA", "buttonB", "prize"])


class Solution(BaseSolution):

    @classmethod
    def _parse_line(cls, line: str) -> tuple[int, int]:
        coords = line.split(":")[1].strip()
        x, y = coords.split(", ")
        return (int(x[2:]), int(y[2:]))

    def init(self) -> None:
        lines = IO.load_lines(self.filename)
        self.machines: List[Machine] = []
        for i in range(0, len(lines), 4):
            machine = Machine(
                self._parse_line(lines[i]),
                self._parse_line(lines[i + 1]),
                self._parse_line(lines[i + 2]),
            )
            self.machines.append(machine)

    def stage1(self) -> int:
        total_tokens: int = 0
        for machine in self.machines:
            prize_x, prize_y = machine.prize
            buttonA_x, buttonA_y = machine.buttonA
            buttonB_x, buttonB_y = machine.buttonB
            visited = set()
            pq = [(0, 0, 0)]  # (cost, x, y)

            while pq:
                cost, x, y = heapq.heappop(pq)
                if (x, y) in visited or x > prize_x or y > prize_y:
                    continue
                visited.add((x, y))

                if x == prize_x and y == prize_y:
                    return cost

                heapq.heappush(pq, (cost + 3, x + buttonA_x, y + buttonA_y))
                heapq.heappush(pq, (cost + 1, x + buttonB_x, y + buttonB_y))

        return total_tokens

    def stage2(self) -> int:
        total_tokens: int = 0
        for machine in self.machines:
            buttonA_x, buttonA_y = machine.buttonA
            buttonB_x, buttonB_y = machine.buttonB
            prize_x, prize_y = machine.prize
            prize_x += 10000000000000
            prize_y += 10000000000000

            det = buttonA_x * buttonB_y - buttonA_y * buttonB_x
            if det == 0:
                return -1

            a = (prize_x * buttonB_y - prize_y * buttonB_x) / det
            b = (buttonA_x * prize_y - buttonA_y * prize_x) / det

            if a >= 0 and b >= 0 and a == int(a) and b == int(b):
                total_tokens += int(3 * a + b)

        return total_tokens


if __name__ == "__main__":
    Solution.main()
