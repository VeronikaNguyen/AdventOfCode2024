import re


class Day3:
    input: list[str]

    def __init__(self, lines: list[str]):
        self.input = lines

    def part1(self) -> int:
        return Day3.do_multiplication_operations(self.match(r'mul\((\d+),(\d+)\)'))

    def part2(self) -> int:
        return Day3.do_multiplication_operations_extended(self.match(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'))

    def match(self, match_pattern: str) -> list[any]:
        match = []
        for line in self.input:
            match += re.findall(match_pattern, line)
        return match

    @staticmethod
    def do_multiplication_operations(match: list[tuple[str, str]]) -> int:
        sum = 0
        for entry in match:
            sum += int(entry[0]) * int(entry[1])
        return sum

    @staticmethod
    def do_multiplication_operations_extended(match: list[tuple[str, str]]) -> int:
        sum = 0
        enable_summing = True
        for entry in match:
            if entry == 'do()':
                enable_summing = True
            elif entry == 'don\'t()':
                enable_summing = False
            elif enable_summing:
                entry_match = re.match(r"mul\((\d+),(\d+)\)", entry)
                sum += int(entry_match.group(1)) * int(entry_match.group(2))
        return sum
