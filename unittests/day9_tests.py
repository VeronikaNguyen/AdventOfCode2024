import unittest

from days.day9 import Day9
from days.utils import FileReader


class TestDay9(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day9")
        day = Day9(reader.read_lines())
        self.assertEqual(day.part1(), 1928)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day9")
        day = Day9(reader.read_lines())
        self.assertEqual(day.part1(), 6398252054886)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day9")
        day = Day9(reader.read_lines())
        self.assertEqual(day.part2(), 2858)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day9")
        day = Day9(reader.read_lines())
        self.assertEqual(day.part2(), 6415666220005)
