import unittest

from days.day1 import Day1
from days.utils import FileReader


class TestDay1(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day1")
        day1 = Day1(reader.read_lines())
        self.assertEqual(day1.part1(), 11)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day1")
        day1 = Day1(reader.read_lines())
        self.assertEqual(day1.part1(), 2344935)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day1")
        day1 = Day1(reader.read_lines())
        self.assertEqual(day1.part2(), 31)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day1")
        day1 = Day1(reader.read_lines())
        self.assertEqual(day1.part2(), 27647262)
