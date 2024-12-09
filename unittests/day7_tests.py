import unittest

from days.day7 import Day7
from days.utils import FileReader


class TestDay7(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_day7")
        day = Day7(reader.read_lines())
        self.assertEqual(day.part1(), 3749)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_day7")
        day = Day7(reader.read_lines())
        self.assertEqual(day.part1(), 5837374519342)

    def test_part2(self):
        reader = FileReader("testdata/testdata_day7")
        day = Day7(reader.read_lines())
        self.assertEqual(day.part2(), 11387)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_day7")
        day = Day7(reader.read_lines())
        self.assertEqual(day.part2(), 492383931650959)
