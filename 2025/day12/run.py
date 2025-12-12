import numpy as np
import numpy.typing as npt
from typing import List, NamedTuple, Tuple

from aoc.base_solution import BaseSolution


class Present(NamedTuple):
    shape: npt.NDArray[np.bool]


class Region(NamedTuple):
    dimensions: Tuple[int, int]
    quantities: List[int]


class Solution(BaseSolution):

    def init(self) -> None:
        lines = self.load_lines()
        self.presents: List[Present] = []
        for i in range(0, 30, 5):
            shape = np.array([[c == "#" for c in lines[i + r]] for r in range(1, 4)])
            self.presents.append(Present(shape=shape))

        self.regions: List[Region] = []
        for line in lines[30:]:
            dimensions, quantities = line.split(": ")
            width, height = dimensions.split("x")
            region = Region(
                dimensions=(int(width), int(height)),
                quantities=list(map(int, quantities.split(" "))),
            )
            self.regions.append(region)

    def _try_place_present(
        self,
        present: npt.NDArray[np.bool],
        grid: npt.NDArray[np.bool],
        r: int,
        c: int,
        presents_count: List[int],
    ) -> bool:
        h, w = present.shape
        if grid[r : r + h, c : c + w].shape == present.shape:
            has_overlap = np.any(present & grid[r : r + h, c : c + w])
            if not has_overlap:
                grid_copy = grid.copy()
                grid_copy[r : r + h, c : c + w] |= present
                return self._place_presents(presents_count, grid_copy)
        return False

    def _place_presents(
        self, presents_count: List[int], grid: npt.NDArray[np.bool]
    ) -> bool:
        if not any(presents_count):
            return True

        for i in range(6):
            if not presents_count[i]:
                continue

            temp_presents_count = presents_count.copy()
            temp_presents_count[i] -= 1

            present = self.presents[i].shape
            for r, c in np.ndindex(grid.shape):
                for _ in range(4):
                    if self._try_place_present(
                        present, grid, r, c, temp_presents_count
                    ):
                        return True
                    present = np.rot90(present)

        return False

    def stage1(self) -> int:
        # Real Attempt:
        #
        # valid_count = 0
        # for region in self.regions:
        #     width, height = region.dimensions
        #     grid: npt.NDArray[np.bool] = np.array(
        #         [[False] * (width) for _ in range(height)]
        #     )
        #     result = self._place_presents(region.quantities, grid)
        #     valid_count += result
        # return valid_count
        #
        # This was running very slowly. Claude pointed me towards Donald Knuth's
        # Algorithm X with Dancing Links, which seemed to speed things up a bit.
        #
        #
        # Dumb Attempt, after realizing the input was a complete gimme.

        valid_count = 0
        for region in self.regions:
            width, height = region.dimensions
            available_blocks = (width // 3) * (height // 3)
            required_blocks = sum(region.quantities)
            valid_count += available_blocks >= required_blocks

        return valid_count

    def stage2(self) -> int: ...


if __name__ == "__main__":
    Solution.main()
