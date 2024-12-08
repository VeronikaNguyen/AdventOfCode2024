import copy


class Day6:
    grid: list[str]
    start_position: tuple[int, int]
    visited_positions: set[tuple[int, int]]

    def __init__(self, lines: list[str]):
        self.grid = lines
        self.create_edges('X')
        self.determine_start_position()
        self.visited_positions, _ = self.determine_if_guard_is_in_loop(self.grid, self.start_position)

    def part1(self) -> int:
        return len(self.visited_positions)

    def part2(self) -> int:
        sum = 0
        for position in self.visited_positions:
            if position == self.start_position:
                continue
            temp_grid = copy.deepcopy(self.grid)
            temp_grid[position[0]] = temp_grid[position[0]][:position[1]] + '#' + temp_grid[position[0]][position[1]+1:]
            _, in_loop = self.determine_if_guard_is_in_loop(temp_grid, self.start_position)
            sum += in_loop
        return sum

    def create_edges(self, character: chr) -> None:
        edge = character * len(self.grid[0])
        self.grid.insert(0, edge)
        self.grid.append(edge)
        for idx, line in enumerate(self.grid):
            self.grid[idx] = character + line + character

    def determine_start_position(self) -> None:
        for x, line in enumerate(self.grid):
            for y, character in enumerate(line):
                if character == '^':
                    self.start_position = (x, y)
                    return

    @staticmethod
    def determine_if_guard_is_in_loop(grid: list[str], start_position: tuple[int, int]) -> (set[tuple[int, int]], bool):
        visited_positions = set()
        visited_configurations = set()
        config = (start_position, (-1, 0))
        while config not in visited_configurations:
            visited_configurations.add(config)
            current_position, direction = config
            visited_positions.add(current_position)
            new_position_if_valid = (current_position[0] + direction[0], current_position[1] + direction[1])
            if grid[new_position_if_valid[0]][new_position_if_valid[1]] == '#':
                direction = Day6.rotate_direction(direction)
                config = (current_position, direction)
            elif grid[new_position_if_valid[0]][new_position_if_valid[1]] == 'X':
                return visited_positions, False
            else:
                config = (new_position_if_valid, direction)
        return visited_positions, True

    @staticmethod
    def rotate_direction(direction: tuple[int, int]) -> tuple[int, int]:
        match direction:
            case (-1, 0):
                return (0, 1)
            case (1, 0):
                return (0, -1)
            case (0, 1):
                return (1, 0)
            case (0, -1):
                return (-1, 0)
