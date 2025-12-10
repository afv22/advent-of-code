import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from collections import deque
from typing import List, NamedTuple

from aoc.base_solution import BaseSolution


class Machine(NamedTuple):
    lights: tuple[bool, ...]
    buttons: List[set[int]]
    joltage: List[int]


class Solution(BaseSolution):

    def init(self) -> None:
        self.machines: List[Machine] = []
        for line in self.load_lines():
            chunks = line.split(" ")
            lights = tuple(light == "#" for light in chunks[0].strip("[]"))
            buttons = []
            for button in chunks[1:-1]:
                button = set(int(n) for n in button.strip("()").split(","))
                buttons.append(button)
            joltage = [int(n) for n in chunks[-1].strip("{}").split(",")]
            self.machines.append(Machine(lights, buttons, joltage))

    def stage1(self) -> int:
        total_presses = 0
        for machine in self.machines:
            lights_target, buttons, _ = machine
            initial_state = tuple([False] * len(lights_target))
            states = deque([(initial_state, 0)])
            seen_states = set()

            while states:
                state, presses = states.popleft()
                seen_states.add(state)

                if state == lights_target:
                    total_presses += presses
                    break

                for button in buttons:
                    new_state = tuple(
                        not light if i in button else light
                        for i, light in enumerate(state)
                    )
                    if new_state not in seen_states:
                        states.append((new_state, presses + 1))

        return total_presses

    def stage2(self) -> int:
        total_presses = 0
        for machine in self.machines:
            n_buttons, n_counters = len(machine.buttons), len(machine.joltage)

            A = np.zeros((n_counters, n_buttons))
            for j, button in enumerate(machine.buttons):
                for i in button:
                    A[i, j] = 1

            # Objective Function: Solver minimizes c_0 * x_0 + c_1 * x_1 + ...
            # Since we don't want to scale any of the results, we use all ones
            c = np.ones(n_buttons)

            # Constraint: Describes the final result. Since we want an exact value
            #   instead of a range, the lower and upper bounds are equal
            constraints = LinearConstraint(A, machine.joltage, machine.joltage)  # type: ignore

            # Bounds: Describes each individual variable. A button can be pressed
            #   between 0 and infinity times
            bounds = Bounds(lb=0, ub=np.inf)

            # Integrality: milp-specific configuration for whether the results
            #   need to be integers or nots
            integrality = np.ones(n_buttons)

            result = milp(
                c, constraints=constraints, bounds=bounds, integrality=integrality
            )
            total_presses += int(round(result.fun))

        return total_presses


if __name__ == "__main__":
    Solution.main()
