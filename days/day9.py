import copy


class Day9:
    disk: list[int]
    free_space: dict[int, int]
    insertion_data: dict[int, int]
    initial_disk_idx: dict[int, int]

    def __init__(self, lines: list[str]):
        self.disk = []
        self.insertion_data = dict()
        self.free_space = dict()
        self.initial_disk_idx = dict()
        self.parse_input([int(num) for num in list(lines[0])])

    def part1(self) -> int:
        return self.compute_checksum(self.move_disk_space_partial())

    def part2(self) -> int:
        return self.compute_checksum(self.move_disk_space_whole())

    def parse_input(self, input: list[int]) -> None:
        counter = 0
        for idx, number in enumerate(input):
            if idx % 2 == 0:
                self.initial_disk_idx[counter] = len(self.disk)
                for _ in range(number):
                    self.disk.append(counter)
                    self.insertion_data[counter] = number
                counter += 1
            else:
                if number != 0:
                    self.free_space[len(self.disk)] = number
                for _ in range(number):
                    self.disk.append(-1)

    def move_disk_space_partial(self) -> list[int]:
        modified_disk = copy.deepcopy(self.disk)
        start_idx_free_space = 0
        for back_idx in range(len(modified_disk) - 1, -1, -1):
            if start_idx_free_space >= back_idx:
                break
            elif modified_disk[back_idx] == -1:
                continue
            element = modified_disk.pop(back_idx)
            for front_idx in range(start_idx_free_space, back_idx):
                if modified_disk[front_idx] == -1:
                    start_idx_free_space = front_idx + 1
                    modified_disk[front_idx] = element
                    break
        return modified_disk

    def move_disk_space_whole(self) -> list[int]:
        modified_disk = copy.deepcopy(self.disk)
        for insertion_value, insertion_times in sorted(self.insertion_data.items(), reverse=True):
            inserted = False
            for free_idx, free_times in sorted(self.free_space.items()):
                if self.initial_disk_idx[insertion_value] < free_idx:
                    break
                if free_times >= insertion_times:
                    del self.free_space[free_idx]
                    remaining_insertions = free_times - insertion_times
                    if remaining_insertions > 0:
                        self.free_space[free_idx + insertion_times] = remaining_insertions
                    for idx in range(free_idx, free_idx + insertion_times):
                        modified_disk[idx] = insertion_value
                    inserted = True
                    break
            if inserted:
                back_idx = self.initial_disk_idx[insertion_value]
                for idx in range(back_idx, back_idx + insertion_times):
                    modified_disk[idx] = -1
        return modified_disk

    @staticmethod
    def compute_checksum(input: list[int]) -> int:
        sum = 0
        for idx, entry in enumerate(input):
            if entry == -1:
                continue
            sum += idx * entry
        return sum