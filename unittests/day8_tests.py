import unittest

from days.day8 import Day8
from days.utils import FileReader


class TestDay8(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day8")
        day = Day8(reader.read_lines())
        self.assertEqual(day.part1(), 14)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day8")
        day = Day8(reader.read_lines())
        self.assertEqual(day.part1(), 265)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day8")
        day = Day8(reader.read_lines())
        self.assertEqual(day.part2(), 34)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day8")
        day = Day8(reader.read_lines())
        self.assertEqual(day.part2(), 0)
