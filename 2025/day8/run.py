import math
from collections import namedtuple
from solution import BaseSolution
from typing import List

Box = namedtuple("Box", ["x", "y", "z"])


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure with path compression and union by size."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        """Find the root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """Union two sets by size."""
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        # Union by size: attach smaller tree to larger tree
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

    def get_component_sizes(self) -> List[int]:
        """Get sizes of all connected components."""
        roots = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in roots:
                roots[root] = self.size[root]
        return list(roots.values())


class Solution(BaseSolution):

    def init(self) -> None:
        self.boxes: List[Box] = []
        with open(self.filename, "r") as f:
            for line in f.readlines():
                x, y, z = line.strip().split(",")
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
