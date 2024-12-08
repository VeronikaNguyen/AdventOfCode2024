import unittest

from days.day5 import Day5
from days.utils import FileReader


class TestDay5(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day5")
        day = Day5(reader.read_lines())
        self.assertEqual(day.part1(), 143)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day5")
        day = Day5(reader.read_lines())
        self.assertEqual(day.part1(), 4135)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day5")
        day = Day5(reader.read_lines())
        self.assertEqual(day.part2(), 123)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day5")
        day = Day5(reader.read_lines())
        self.assertEqual(day.part2(), 5285)
