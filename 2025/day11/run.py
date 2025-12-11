from aoc.base_solution import BaseSolution


class Solution(BaseSolution):

    EXAMPLE_FILE_2 = "./example2.txt"

    def init(self) -> None:
        self.machines: dict[str, list[str]] = {}
        for line in self.load_lines():
            id, outputs = line.split(": ")
            self.machines[id] = outputs.split(" ")

    _memo = {}

    def _dfs(self, id: str, target: str) -> int:
        if id == target:
            return 1

        if id == "out":
            return 0

        if (id, target) in self._memo:
            return self._memo[(id, target)]

        paths = sum(self._dfs(conn_id, target) for conn_id in self.machines[id])
        self._memo[(id, target)] = paths
        return paths

    def stage1(self) -> int:
        return self._dfs("you", "out")

    def stage2(self) -> int:
        # SVR -> FFT -> DAC -> OUT
        svr_fft = self._dfs("svr", "fft")
        fft_dac = self._dfs("fft", "dac")
        dac_out = self._dfs("dac", "out")

        # SVR -> DAC -> FFT -> OUT
        svr_dac = self._dfs("svr", "dac")
        dac_fft = self._dfs("dac", "fft")
        fft_out = self._dfs("fft", "out")

        return svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out


if __name__ == "__main__":
    Solution.main()
