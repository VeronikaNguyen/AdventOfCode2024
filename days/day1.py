from collections import defaultdict

class Day1:
    left_list: list[int]
    right_list: list[int]
    left_number_to_count_map: defaultdict[int, int]
    right_number_to_count_map: defaultdict[int, int]

    def __init__(self, lines: list[str]):
        self.left_list = []
        self.right_list = []
        self.left_number_to_count_map = defaultdict(int)
        self.right_number_to_count_map = defaultdict(int)
        self.parse_input(lines)
        self.prepare_input()

    def part1(self) -> int:
        return self.compute_total_distance_between_lists()

    def part2(self) -> int:
        return self.compute_total_similarity_between_lists()

    def parse_input(self, lines: list[str]) -> None:
        for line in lines:
            [left, right] = line.split()
            self.left_list.append(int(left))
            self.right_list.append(int(right))

    def prepare_input(self) -> None:
        self.left_list.sort()
        self.right_list.sort()

        for left_entry in self.left_list:
            self.left_number_to_count_map[left_entry] += 1

        for right_entry in self.right_list:
            self.right_number_to_count_map[right_entry] += 1

    def compute_total_distance_between_lists(self) -> int:
        total_distance = 0
        for idx in range(len(self.left_list)):
            total_distance += abs(self.left_list[idx] - self.right_list[idx])
        return total_distance

    def compute_total_similarity_between_lists(self) -> int:
        total_similarity = 0
        for key in self.left_number_to_count_map:
            total_similarity += key * self.left_number_to_count_map[key] * self.right_number_to_count_map[key]
        return total_similarity
