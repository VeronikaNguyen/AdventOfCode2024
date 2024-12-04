import unittest

from days.day4 import Day4
from days.utils import FileReader


class TestDay4(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day4")
        day = Day4(reader.read_lines())
        self.assertEqual(day.part1(), 18)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day4")
        day = Day4(reader.read_lines())
        self.assertEqual(day.part1(), 2639)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day4")
        day = Day4(reader.read_lines())
        self.assertEqual(day.part2(), 9)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day4")
        day = Day4(reader.read_lines())
        self.assertEqual(day.part2(), 2005)
