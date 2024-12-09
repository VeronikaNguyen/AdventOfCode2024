import copy
import operator


class Day7:
    results: list[int]
    numbers: list[list[int]]

    def __init__(self, lines: list[str]):
        self.results = []
        self.numbers = []
        self.parse_input(lines)

    def part1(self) -> int:
        return self.sum_results([operator.add, operator.mul])

    def part2(self) -> int:
        return self.sum_results([self.concatenation_operator, operator.mul, operator.add])

    def sum_results(self, operators: list[operator]) -> int:
        sum = 0
        for idx, result in enumerate(self.results):
            numbers = copy.deepcopy(self.numbers[idx])
            assert(len(numbers) > 0)
            if self.determine_if_result_is_possible(result, numbers, numbers.pop(0), operators):
                sum += result
        return sum

    def parse_input(self, lines: list[str]) -> None:
        for line in lines:
            result, numbers = line.split(':')
            self.results.append(int(result))
            self.numbers.append([int(number) for number in numbers.split()])

    @staticmethod
    def determine_if_result_is_possible(result: int, numbers: list[int], current_number: int, operators: list[operator]) -> bool:
        if len(numbers) == 0:
            return result == current_number
        elif current_number > result:
            return False

        popped_number = numbers.pop(0)
        for op in operators:
            if Day7.determine_if_result_is_possible(result, copy.deepcopy(numbers), op(current_number, popped_number), operators):
                return True
        return False

    @staticmethod
    def concatenation_operator(first_number: int, second_number: int) -> int:
        return int(str(first_number) + str(second_number))
