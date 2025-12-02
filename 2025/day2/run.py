from typing import List


INPUT_FILE = "./input.txt"
EXAMPLE_FILE = "./example.txt"


def load_input() -> List[tuple[int, int]]:
    with open(INPUT_FILE, "r") as f:
        s = f.read().strip()

    raw_ranges = s.split(",")
    ranges: List[tuple[int, int]] = []
    for rr in raw_ranges:
        low, high = rr.split("-")
        ranges.append((int(low), int(high)))

    return ranges


def stage1(ranges) -> int:
    total = 0
    for low, high in ranges:
        for n in range(low, high + 1):
            s = str(n)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                if s[:mid] == s[mid:]:
                    total += n

    return total


def stage2(ranges) -> int:
    total = 0
    # For each range
    for low, high in ranges:
        # For each number in that range
        for n in range(low, high + 1):
            s = str(n)
            # For each chunk in that number
            for chunk_size in range(1, (len(s) // 2) + 1):
                if len(s) % chunk_size == 0:
                    # Check for repeating pattern
                    pattern = s[:chunk_size]
                    if pattern * (len(s) // chunk_size) == s:
                        total += n
                        break

    return total


def main() -> None:
    ranges = load_input()

    print("Stage 1:", stage1(ranges))
    print("Stage 2:", stage2(ranges))


if __name__ == "__main__":
    main()
