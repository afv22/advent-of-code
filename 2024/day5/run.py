from collections import defaultdict
from typing import Dict, List, Set
from functools import cmp_to_key

INPUT_FILE = "./input.txt"


def load_input() -> tuple[Dict[int, Set[int]], List[List[int]]]:
    rules = defaultdict(set)
    updates = []
    with open(INPUT_FILE, "r") as f:
        for line in f.readlines():
            if "|" in line:
                n1, n2 = line.split("|")
                rules[int(n1)].add(int(n2))
            elif line != "\n":
                updates.append([int(n) for n in line.split(",")])

    return (rules, updates)


def stage1(rules: Dict[int, Set[int]], updates: List[List[int]]) -> None:
    middle_number_sum = 0
    for update in updates:
        seen = set()
        is_valid = True
        for n in update:
            if rules[n].intersection(seen):
                is_valid = False
                break
            seen.add(n)

        if is_valid:
            middle_number = update[len(update) // 2]
            middle_number_sum += middle_number

    print("Middle Numbers:", middle_number_sum)


def stage2(rules: Dict[int, Set[int]], updates: List[List[int]]) -> None:

    def _comparison(a, b):
        if a in rules and b in rules[a]:
            return -1
        if b in rules and a in rules[b]:
            return 1
        return 0

    middle_number_sum = 0
    for update in updates:
        seen = set()
        is_valid = True
        for n in update:
            if rules[n].intersection(seen):
                is_valid = False
                break
            seen.add(n)

        if not is_valid:
            update.sort(key=cmp_to_key(_comparison))
            middle_number = update[len(update) // 2]
            middle_number_sum += middle_number

    print("Middle Numbers:", middle_number_sum)


def main() -> None:
    rules, updates = load_input()

    stage1(rules, updates)
    stage2(rules, updates)


if __name__ == "__main__":
    main()
