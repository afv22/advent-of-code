INPUT_FILE = "./input.txt"
EXAMPLE_FILE = "./example.txt"


def load_input() -> str:
    with open(INPUT_FILE, "r") as f:
        s = f.read()

    return s


def stage1(input) -> int:
    return -1


def stage2(input) -> int:
    return -1


def main() -> None:
    input = load_input()

    print("Stage 1:", stage1(input))
    print("Stage 2:", stage2(input))


if __name__ == "__main__":
    main()
