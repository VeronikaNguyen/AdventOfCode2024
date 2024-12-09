import unittest

from days.dayX import DayX
from days.utils import FileReader


class TestDayX(unittest.TestCase):
    def test_part1(self):
        reader = FileReader("testdata/testdata_dayX")
        day = DayX(reader.read_lines())
        self.assertEqual(day.part1(), 0)

    def test_part1_solution(self):
        reader = FileReader("testdata/data_dayX")
        day = DayX(reader.read_lines())
        self.assertEqual(day.part1(), 0)

    def test_part2(self):
        reader = FileReader("testdata/testdata_dayX")
        day = DayX(reader.read_lines())
        self.assertEqual(day.part2(), 0)

    def test_part2_solution(self):
        reader = FileReader("testdata/data_dayX")
        day = DayX(reader.read_lines())
        self.assertEqual(day.part2(), 0)
