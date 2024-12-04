from collections import defaultdict
import re


class Day4:
    input: list[str]

    def __init__(self, lines: list[str]):
        self.input = lines
        self.match_string = "XMAS"

    def part1(self) -> int:
        return self.count_xmas()

    def part2(self) -> int:
        return self.count_x_mas()

    def match(self, match_pattern: str) -> list[any]:
        match = []
        for line in self.input:
            match += re.findall(match_pattern, line)
        return match

    def is_xmas_in_direction(self, position: tuple[int, int], direction: tuple[int, int]) -> bool:
        for idx in range(len(self.match_string)):
            x, y = position
            x += idx * direction[0]
            y += idx * direction[1]
            if 0 > x or x >= len(self.input) or 0 > y or y >= len(self.input[0]):
                return False
            if self.input[x][y] != self.match_string[idx]:
                return False
        return True

    def is_x_mas(self, position: tuple[int, int]) -> bool:
        if not self.is_mas_in_diag(position, [(1, 1), (-1, -1)]):
            return False
        if not self.is_mas_in_diag(position, [(1, -1), (-1, 1)]):
            return False
        return True

    def is_mas_in_diag(self, position: tuple[int, int], diag: list[tuple[int, int]]) -> bool:
        diag_map = defaultdict(int)
        for direction in diag:
            x, y = position
            x += direction[0]
            y += direction[1]
            if 0 > x or x >= len(self.input) or 0 > y or y >= len(self.input[0]):
                return False
            diag_map[self.input[x][y]] += 1
        if diag_map['M'] == 1 and diag_map['S'] == 1:
            return True
        else:
            return False

    def count_xmas(self) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        sum = 0
        for x in range(len(self.input)):
            for y in range(len(self.input[0])):
                for direction in directions:
                    if self.input[x][y] == "X":
                        sum += self.is_xmas_in_direction((x, y), direction)
        return sum

    def count_x_mas(self) -> int:
        sum = 0
        for x in range(len(self.input)):
            for y in range(len(self.input[0])):
                if self.input[x][y] == "A":
                    sum += self.is_x_mas((x, y))
        return sum
