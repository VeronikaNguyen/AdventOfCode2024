class Day2:
    numbers: list[list[int]]

    def __init__(self, lines: list[str]):
        self.parse_input(lines)

    def part1(self) -> int:
        return self.count_number_of_safe_reports(False)

    def part2(self) -> int:
        return self.count_number_of_safe_reports(True)

    def parse_input(self, lines: list[str]) -> None:
        self.numbers = [list(map(int, line.split())) for line in lines]

    def count_number_of_safe_reports(self, with_tolerance: bool) -> int:
        number_of_safe_reports = 0
        for report in self.numbers:
            if with_tolerance:
                number_of_safe_reports += int(self.determine_if_report_is_safe_with_tolerance(report))
            else:
                number_of_safe_reports += int(self.determine_if_report_is_safe(report))
        return number_of_safe_reports

    @staticmethod
    def determine_if_report_is_safe(report: list[int]) -> bool:
        assert (len(report) >= 2)
        increasing = (report[1] > report[0])
        for idx in range(len(report) - 1):
            diff = (report[idx + 1] - report[idx])
            if 1 <= diff <= 3 and increasing:
                continue
            elif -3 <= diff <= -1 and not increasing:
                continue
            else:
                return False
        return True

    @staticmethod
    def determine_if_report_is_safe_with_tolerance(report: list[int]) -> bool:
        for idx in range(len(report)):
            if Day2.determine_if_report_is_safe(report[:idx] + report[idx + 1:]):
                return True
        return False
