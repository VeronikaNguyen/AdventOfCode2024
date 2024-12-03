import unittest

from days.day3 import Day3
from days.utils import FileReader


class TestDay3(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day3")
        day = Day3(reader.read_lines())
        self.assertEqual(day.part1(), 161)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day3")
        day = Day3(reader.read_lines())
        self.assertEqual(day.part1(), 166905464)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day3")
        day = Day3(reader.read_lines())
        self.assertEqual(day.part2(), 161)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day3")
        day = Day3(reader.read_lines())
        self.assertEqual(day.part2(), 72948684)
