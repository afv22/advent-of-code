from typing import List

INPUT_FILE = "./input.txt"
EXAMPLE_FILE = "./example.txt"


def load_input() -> List[str]:
    banks: List[str] = []
    with open(INPUT_FILE, "r") as f:
        for bank in f.readlines():
            banks.append(bank.strip())
    return banks


def stage1(banks: List[str]) -> int:
    total = 0
    for bank in banks:
        l, r = bank[-2:]
        for n in bank[:-2][::-1]:
            if n >= l:
                l, r = n, max(l, r)
        total += int(l + r)
    return total


def stage2(banks: List[str]) -> int:
    def propagate(n: str, enabled: str) -> str:
        if not enabled or n < enabled[0]:
            return enabled
        return n + propagate(enabled[0], enabled[1:])

    total = 0
    for bank in banks:
        enabled = bank[-12:]
        for n in bank[:-12][::-1]:
            enabled = propagate(n, enabled)
        total += int(enabled)
    return total


def main() -> None:
    input = load_input()

    print("Stage 1:", stage1(input))
    print("Stage 2:", stage2(input))


if __name__ == "__main__":
    main()
