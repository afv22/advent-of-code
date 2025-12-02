from typing import List
from collections import Counter

INPUT_FILE = "./input.txt"


def load_lists() -> tuple[List, List]:
    l1, l2 = [], []
    with open(INPUT_FILE, "r") as f:
        for line in f:
            n, m = line.split()
            l1.append(int(n))
            l2.append(int(m))

    return (l1, l2)


def stage1(l1, l2) -> None:
    if len(l1) != len(l2):
        raise RuntimeError("Lists are different sizes")

    l1.sort()
    l2.sort()

    total_distance = 0
    for n1, n2 in zip(l1, l2):
        total_distance += abs(n1 - n2)

    print("Distance:", total_distance)


def stage2(l1, l2) -> None:
    c2 = Counter(l2)

    similarity_score = 0
    for n in l1:
        similarity_score += n * c2[n]

    print("Similarity:", similarity_score)


def main() -> None:
    l1, l2 = load_lists()

    stage1(l1, l2)
    stage2(l1, l2)


if __name__ == "__main__":
    main()
