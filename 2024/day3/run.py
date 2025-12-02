import heapq
import regex as re


INPUT_FILE = "./input.txt"

MULT_PATTERN = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
DO_PATTERN = re.compile(r"do\(\)")
DONT_PATTERN = re.compile(r"don\'t\(\)")


def load_program() -> str:
    with open(INPUT_FILE, "r") as f:
        program = f.read()

    return program


def stage1(program) -> None:
    print("Starting Stage 1...")

    result = 0
    for match in re.findall(MULT_PATTERN, program):
        n, m = match[4:-1].split(",")
        result += int(n) * int(m)

    print("Total:", result)


def stage2(program) -> None:
    print("Starting Stage 2...")

    dos = [(m.start(0), True) for m in re.finditer(DO_PATTERN, program)]
    donts = [(m.start(0), False) for m in re.finditer(DONT_PATTERN, program)]

    dos_and_donts = dos + donts
    heapq.heapify(dos_and_donts)

    result = 0
    doing = True
    for match in re.finditer(MULT_PATTERN, program):
        i = match.start()
        while dos_and_donts and i > dos_and_donts[0][0]:
            doing = heapq.heappop(dos_and_donts)[1]

        if not doing:
            continue

        n, m = match.group()[4:-1].split(",")
        result += int(n) * int(m)

    print("Total:", result)


def main() -> None:
    program = load_program()

    stage1(program)
    stage2(program)

    print()


if __name__ == "__main__":
    main()
