import unittest

from days.day2 import Day2
from days.utils import FileReader


class TestDay2(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day2")
        day = Day2(reader.read_lines())
        self.assertEqual(day.part1(), 2)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day2")
        day = Day2(reader.read_lines())
        self.assertEqual(day.part1(), 257)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day2")
        day = Day2(reader.read_lines())
        self.assertEqual(day.part2(), 4)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day2")
        day = Day2(reader.read_lines())
        self.assertEqual(day.part2(), 328)
