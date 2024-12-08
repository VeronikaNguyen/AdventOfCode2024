import unittest

from days.day6 import Day6
from days.utils import FileReader


class TestDay6(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day6")
        day = Day6(reader.read_lines())
        self.assertEqual(day.part1(), 41)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day6")
        day = Day6(reader.read_lines())
        self.assertEqual(day.part1(), 4580)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day6")
        day = Day6(reader.read_lines())
        self.assertEqual(day.part2(), 6)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day6")
        day = Day6(reader.read_lines())
        self.assertEqual(day.part2(), 1480)
