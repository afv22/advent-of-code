from typing import List

INPUT_FILE = "./input.txt"


def load_reports() -> List[int]:
    reports = []
    with open(INPUT_FILE, "r") as f:
        for line in f:
            reports.append([int(n) for n in line.split()])

    return reports


def stage1(reports) -> None:
    print("Starting Stage 1...")
    n_safe = 0
    for report in reports:
        direction = 0
        is_safe = True

        for i, n in enumerate(report[1:], start=1):
            local_direction = -1 if n < report[i - 1] else 1
            if not direction:
                direction = local_direction
            elif direction != local_direction:
                is_safe = False
                break

            if local_direction == -1:
                delta = report[i - 1] - n
            else:
                delta = n - report[i - 1]

            if delta < 1 or delta > 3:
                is_safe = False
                break

        if is_safe:
            n_safe += 1

    print("# Safe:", n_safe)


def stage2(reports) -> None:
    print("Starting Stage 2...")

    def valid_report(report) -> bool:
        direction = 0
        is_safe = True

        for i, n in enumerate(report[1:], start=1):
            local_direction = -1 if n < report[i - 1] else 1
            if not direction:
                direction = local_direction
            elif direction != local_direction:
                is_safe = False
                break

            if local_direction == -1:
                delta = report[i - 1] - n
            else:
                delta = n - report[i - 1]

            if delta < 1 or delta > 3:
                is_safe = False
                break

        return is_safe

    n_safe = 0
    for report in reports:
        if valid_report(report):
            n_safe += 1
        else:
            for i in range(len(report)):
                if valid_report(report[:i] + report[i + 1 :]):
                    n_safe += 1
                    break

    print("# Safe:", n_safe)


def main() -> None:
    reports = load_reports()

    print(f"\nProcessing {len(reports)} reports...")

    stage1(reports)
    stage2(reports)

    print()


if __name__ == "__main__":
    main()
