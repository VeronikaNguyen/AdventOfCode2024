import unittest

from days.day14 import Day14
from days.utils import FileReader


class TestDay14(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day14")
        day = Day14(reader.read_lines(), 11, 7)
        self.assertEqual(day.part1(), 12)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day14")
        day = Day14(reader.read_lines(), 101, 103)
        self.assertEqual(day.part1(), 216027840)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day14")
        day = Day14(reader.read_lines(), 101, 103)
        day.part2(6876)
