import math
from collections import namedtuple
from typing import List

from aoc.base_solution import BaseSolution
from aoc.data_structures import UnionFind

Box = namedtuple("Box", ["x", "y", "z"])


class Solution(BaseSolution):

    def init(self) -> None:
        self.boxes: List[Box] = []
        for line in self.load_lines():
            x, y, z = line.split(",")
            self.boxes.append(Box(int(x), int(y), int(z)))

    @staticmethod
    def _distance(a: Box, b: Box) -> float:
        """Calculate squared Euclidean distance (avoids sqrt for efficiency)."""
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2

    def _get_sorted_distances(self) -> List[tuple[float, int, int]]:
        """Build sorted list of all pairwise distances with box indices."""
        distances = []
        for i in range(len(self.boxes)):
            for j in range(i + 1, len(self.boxes)):
                distances.append((self._distance(self.boxes[i], self.boxes[j]), i, j))
        return sorted(distances)

    def stage1(self) -> int:
        distances = self._get_sorted_distances()
        uf = UnionFind(len(self.boxes))

        connection_limit = 10 if self.use_example else 1000
        for _, box_i, box_j in distances[:connection_limit]:
            uf.union(box_i, box_j)

        circuit_sizes = uf.get_component_sizes()
        return math.prod(sorted(circuit_sizes)[-3:])

    def stage2(self) -> int:
        n_boxes = 20 if self.use_example else 1000
        distances = self._get_sorted_distances()
        uf = UnionFind(len(self.boxes))

        for _, box_i, box_j in distances:
            uf.union(box_i, box_j)

            # Check if all boxes are in one component
            if uf.size[uf.find(0)] == n_boxes:
                return self.boxes[box_i].x * self.boxes[box_j].x
        return -1


if __name__ == "__main__":
    Solution.main()
