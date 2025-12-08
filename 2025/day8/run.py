import math
import heapq
from collections import namedtuple
from functools import reduce
from solution import BaseSolution
from typing import List

Box = namedtuple("Box", ["x", "y", "z"])


class Solution(BaseSolution):

    def init(self) -> None:
        self.boxes: List[Box] = []
        with open(self.filename, "r") as f:
            for line in f.readlines():
                x, y, z = line.strip().split(",")
                self.boxes.append(Box(int(x), int(y), int(z)))

    @staticmethod
    def _distance(a: Box, b: Box) -> float:
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)

    def _get_distance_heap(self) -> List[tuple[float, Box, Box]]:
        distances: List[tuple[float, Box, Box]] = []
        for i, a in enumerate(self.boxes):
            for b in self.boxes[i + 1 :]:
                heapq.heappush(distances, (self._distance(a, b), a, b))
        return distances

    def _connect_boxes(
        self,
        circuits: dict[int, set[Box]],
        connected_boxes: dict[Box, int],
        boxA: Box,
        boxB: Box,
        max_i: int,
    ) -> int:
        if (
            boxA in connected_boxes
            and boxB in connected_boxes
            and connected_boxes[boxA] != connected_boxes[boxB]
        ):
            circuit_a = connected_boxes[boxA]
            circuit_b = connected_boxes[boxB]
            circuits[circuit_a].update(circuits[circuit_b])
            for box in circuits[circuit_b]:
                connected_boxes[box] = circuit_a
            del circuits[circuit_b]

        # If only one is in a circuit, connect the other
        elif boxA in connected_boxes:
            circuits[connected_boxes[boxA]].add(boxB)
            connected_boxes[boxB] = connected_boxes[boxA]
        elif boxB in connected_boxes:
            circuits[connected_boxes[boxB]].add(boxA)
            connected_boxes[boxA] = connected_boxes[boxB]

        # If neither is in a circuit, create a new circuit
        else:
            max_i += 1
            circuits[max_i] = set([boxA, boxB])
            connected_boxes[boxA] = max_i
            connected_boxes[boxB] = max_i

        return max_i

    def stage1(self) -> int:
        distances = self._get_distance_heap()

        circuits: dict[int, set[Box]] = {}
        connected_boxes: dict[Box, int] = {}
        max_i = 0

        connection_limit = 10 if self.use_example else 1000
        for _ in range(connection_limit):
            _, boxA, boxB = heapq.heappop(distances)
            max_i = self._connect_boxes(circuits, connected_boxes, boxA, boxB, max_i)

        circuit_sizes = [len(circuit) for circuit in circuits.values()]
        return reduce(lambda x, y: x * y, sorted(circuit_sizes)[-3:])

    def stage2(self) -> int:
        n_boxes = 20 if self.use_example else 1000
        distances = self._get_distance_heap()

        circuits: dict[int, set[Box]] = {}
        connected_boxes: dict[Box, int] = {}
        max_i = 0

        while True:
            _, boxA, boxB = heapq.heappop(distances)
            max_i = self._connect_boxes(circuits, connected_boxes, boxA, boxB, max_i)

            if len(circuits) == 1 and len(list(circuits.values())[0]) == n_boxes:
                return boxA.x * boxB.x


if __name__ == "__main__":
    Solution.main()
