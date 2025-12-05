from collections import defaultdict
from typing import Dict, List
from solution import BaseSolution


class Solution(BaseSolution):

    def init(self) -> None:
        self.map: List[str] = []
        with open(self.filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                self.map.append(line)

    def _valid(self, row, col) -> bool:
        return 0 <= col < len(self.map[0]) and 0 <= row < len(self.map)

    def _parse_antennae(self) -> Dict[str, List[tuple[int, int]]]:
        antennae: Dict[str, List[tuple[int, int]]] = defaultdict(list)
        for i, row in enumerate(self.map):
            for j, freq in enumerate(row):
                if freq != ".":
                    antennae[freq].append((j, i))
        return antennae

    def stage1(self) -> int:
        antennae = self._parse_antennae()
        antinodes: set[tuple[int, int]] = set()
        
        for locations in antennae.values():
            for i, (x1, y1) in enumerate(locations, start=1):
                for x2, y2 in locations[i:]:
                    xDelta, yDelta = x1 - x2, y1 - y2
                    if self._valid(x1 + xDelta, y1 + yDelta):
                        antinodes.add((x1 + xDelta, y1 + yDelta))
                    if self._valid(x2 - xDelta, y2 - yDelta):
                        antinodes.add((x2 - xDelta, y2 - yDelta))

        return len(antinodes)

    def stage2(self) -> int:
        antennae = self._parse_antennae()
        antinodes: set[tuple[int, int]] = set()

        for locations in antennae.values():
            for i, (r1, c1) in enumerate(locations, start=1):
                for r2, c2 in locations[i:]:
                    rDelta, cDelta = r1 - r2, c1 - c2
                    r1Copy, c1Copy = r1, c1

                    while self._valid(r1Copy, c1Copy):
                        antinodes.add((r1Copy, c1Copy))
                        r1Copy += rDelta
                        c1Copy += cDelta

                    while self._valid(r2, c2):
                        antinodes.add((r2, c2))
                        r2 -= rDelta
                        c2 -= cDelta

        return len(antinodes)


if __name__ == "__main__":
    Solution.main()
