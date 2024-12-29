import copy
import string


class Day14:
    positions: list[tuple[int, int]]
    velocities: list[tuple[int, int]]
    empty_picture: list[string]
    x_boundary: int
    y_boundary: int

    def __init__(self, lines: list[str], x_boundary: int, y_boundary: int):
        self.positions = []
        self.velocities = []
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.empty_picture = []
        self.initialize_empty_picture()
        self.parse_input(lines)

    def part1(self) -> int:
        return self.compute_safety_factor(self.do_iterations(100))

    def part2(self, iterations: int) -> None:
        self.do_iterations(iterations, True)

    def parse_input(self, lines: list[str]) -> None:
        for line in lines:
            position, velocity = line.split(' ')
            x_position, y_position = position[2:].split(',')
            x_velocity, y_velocity = velocity[2:].split(',')
            self.positions.append((int(x_position), int(y_position)))
            self.velocities.append((int(x_velocity), int(y_velocity)))

    def initialize_empty_picture(self) -> None:
        for _ in range(self.y_boundary):
            self.empty_picture.append(' ' * self.x_boundary)

    def do_iterations(self, iterations: int, print_picture: bool = False) -> None:
        new_positions = copy.deepcopy(self.positions)
        for iteration in range(iterations):
            for idx, position in enumerate(new_positions):
                position_x, position_y = position
                position_x = (position_x + self.velocities[idx][0]) % self.x_boundary
                position_y = (position_y + self.velocities[idx][1]) % self.y_boundary
                new_positions[idx] = (position_x, position_y)
            if print_picture:
                picture, could_be_christmas_tree = self.create_picture(new_positions)
                if could_be_christmas_tree:
                    print(f'Iteration {iteration + 1}: \n')
                    self.print_picture(picture)
                    print('\n\n')
        return new_positions

    def compute_safety_factor(self, positions: list[tuple[int, int]]) -> int:
        quadrant_counters = [0, 0, 0, 0, 0]
        for position in positions:
            quadrant_counters[self.determine_quadrant_for_robot(position)] += 1
        safety_factor = 1
        for counter in quadrant_counters[1:]:
            safety_factor *= counter
        return safety_factor

    def determine_quadrant_for_robot(self, position: tuple[int, int]) -> int:
        if position[0] < self.x_boundary // 2 and position[1] < self.y_boundary // 2:
            return 1
        elif position[0] < self.x_boundary // 2 and position[1] > self.y_boundary // 2:
            return 2
        elif position[0] > self.x_boundary // 2 and position[1] < self.y_boundary // 2:
            return 3
        elif position[0] > self.x_boundary // 2 and position[1] > self.y_boundary // 2:
            return 4
        else:
            return 0

    @staticmethod
    def print_picture(picture: list[string]) -> None:
        for line in picture:
            print(line)

    def create_picture(self, positions: list[tuple[int, int]]) -> (list[string], bool):
        picture = copy.deepcopy(self.empty_picture)
        for position in positions:
            x, y = position[0], position[1]
            if picture[y][x] == ' ':
                picture[y] = picture[y][:x] + '*' + picture[y][x + 1:]
            else:
                return [], False
        return picture, True
