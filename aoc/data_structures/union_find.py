from typing import List


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
