from collections import defaultdict
from enum import Enum


class Variant(Enum):
    NORMAL = 1
    FREQUENT = 2


class Day8:
    map: defaultdict[chr, list[tuple[int, int]]]
    bounds: tuple[int, int]

    def __init__(self, lines: list[str]):
        self.map = defaultdict(list)
        self.parse_input(lines)

    def part1(self) -> int:
        return self.compute_antidotes_for_map(Variant.NORMAL)

    def part2(self) -> int:
        return self.compute_antidotes_for_map(Variant.FREQUENT)

    def parse_input(self, lines) -> None:
        for i, line in enumerate(lines):
            for j, letter in enumerate(line):
                if letter != '.':
                    self.map[letter].append((i, j))
        self.bounds = (len(lines), len(lines[0]))

    def compute_antidotes_for_map(self, variant: Variant) -> int:
        antidotes = set()
        for key in self.map:
            self.compute_antidotes_for_antennas(variant, antidotes, self.map[key])
        return len(antidotes)

    def compute_antidotes_for_antennas(self, variant: Variant, antidotes: set[tuple[int, int]], antennas: list[tuple[int, int]]) -> None:
        for first_idx, first in enumerate(antennas):
            for second in antennas[first_idx + 1:]:
                self.compute_antidotes_for_pair(variant, antidotes, first, second)

    def compute_antidotes_for_pair(self, variant: Variant, antidotes: set[tuple[int, int]], first: tuple[int, int], second: tuple[int, int]) -> None:
        if variant == Variant.NORMAL:
            self.compute_antidotes_for_pair_normal(antidotes, first, second)
        elif variant == Variant.FREQUENT:
            self.compute_antidotes_for_pair_frequent(antidotes, first, second)

    def compute_antidotes_for_pair_frequent(self, antidotes: set[tuple[int, int]], first: tuple[int, int], second: tuple[int, int]) -> None:
        distance = [first[0] - second[0], first[1] - second[1]]
        antidotes.add(first)
        antidotes.add(second)

        in_bounds = True
        while in_bounds:
            first = (first[0] + distance[0], first[1] + distance[1])
            in_bounds = self.add_antidote_if_in_bounds(antidotes, first)

        in_bounds = True
        while in_bounds:
            second = (second[0] - distance[0], second[1] - distance[1])
            in_bounds = self.add_antidote_if_in_bounds(antidotes, second)

    def compute_antidotes_for_pair_normal(self, antidotes: set[tuple[int, int]], first: tuple[int, int], second: tuple[int, int]) -> None:
        distance = [first[0] - second[0], first[1] - second[1]]
        self.add_antidote_if_in_bounds(antidotes, (first[0] + distance[0], first[1] + distance[1]))
        self.add_antidote_if_in_bounds(antidotes, (second[0] - distance[0], second[1] - distance[1]))

    def add_antidote_if_in_bounds(self, antidotes: set[tuple[int, int]], antidote: tuple[int, int]) -> bool:
        if 0 <= antidote[0] < self.bounds[0] and 0 <= antidote[1] < self.bounds[1]:
            antidotes.add(antidote)
            return True
        return False



