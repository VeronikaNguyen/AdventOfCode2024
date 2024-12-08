from collections import defaultdict


class Day5:
    ordering: defaultdict[int, set]
    pages: list[list[int]]
    correct_pages: list[list[int]]
    incorrect_pages: list[list[int]]

    def __init__(self, lines: list[str]):
        self.ordering = defaultdict(set)
        self.pages, self.correct_pages, self.incorrect_pages = [], [], []
        self.parse_input(lines)
        self.determine_correct_and_incorrect_pages()

    def part1(self) -> int:
        return Day5.sum_middle_numbers(self.correct_pages)

    def part2(self) -> int:
        self.order_incorrect_pages()
        return Day5.sum_middle_numbers(self.incorrect_pages)

    def parse_input(self, lines: list[str]) -> None:
        first_part = True
        for line in lines:
            if line == "":
                first_part = False
                continue

            if first_part:
                left, right = line.split('|')
                self.ordering[int(left)].add(int(right))
            else:
                self.pages.append([int(num) for num in line.split(',')])

    def order_incorrect_pages(self) -> None:
        for idx, page in enumerate(self.incorrect_pages):
            self.incorrect_pages[idx] = self.order_page(page)

    def order_page(self, page: list[int]) -> list[int]:
        ordered_page = page
        for current_idx, current_number in enumerate(page):
            for temp_idx, temp_number in enumerate(page[:current_idx]):
                if temp_number in self.ordering[current_number]:
                    ordered_page[current_idx], ordered_page[temp_idx] = page[temp_idx], page[current_idx]
        return ordered_page

    def determine_correct_and_incorrect_pages(self) -> None:
        for page in self.pages:
            if self.determine_if_page_is_correct(page):
                self.correct_pages.append(page)
            else:
                self.incorrect_pages.append(page)

    def determine_if_page_is_correct(self, page: list[int]) -> bool:
        for idx, current_number in enumerate(page):
            for temp_number in page[:idx]:
                if temp_number in self.ordering[current_number]:
                    return False
        return True

    @staticmethod
    def sum_middle_numbers(pages: list[list[int]]) -> int:
        sum = 0
        for page in pages:
            sum += page[len(page) // 2]
        return sum
