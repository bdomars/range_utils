import unittest
import ranges

from datetime import datetime


class MergeTests(unittest.TestCase):

    def test_merge_ranges(self):
        list_of_ranges = [(2, 5), (3, 6), (8, 10)]
        merged_ranges = ranges.merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(2, 6), (8, 10)])

    def test_merge_ranges_with_none(self):
        list_of_ranges = [(None, 5), (3, 6), (8, None)]
        merged_ranges = ranges.merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, 6), (8, None)])

    def test_merge_ranges_unordered(self):
        list_of_ranges = [(2, 3), (1, 4), (7, 11), (6, 12)]
        merged_ranges = ranges.merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(1, 4), (6, 12)])

    def test_merge_ranges_unordered_with_none(self):
        list_of_ranges = [(2, 3), (None, 4), (7, None), (6, 12)]
        merged_ranges = ranges.merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, 4), (6, None)])

    def test_merge_ranges_empty(self):
        list_of_ranges = []
        merged_ranges = ranges.merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [])

    def test_merge_ranges_continuous(self):
        list_of_ranges = [(2, 6), (6, 9), (1, 2)]
        merged_ranges = ranges.merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(1, 9)])

    def test_merge_ranges_continuous_with_none(self):
        list_of_ranges = [(None, 2), (2, None), (6, 9)]
        merged_ranges = ranges.merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, None)])

    def test_merge_ranges_dt(self):
        list_of_ranges = [(datetime(1990, 2, 1), datetime(1990, 2, 15)), (datetime(1990, 2, 15), datetime(1990, 2, 27))]
        merged_ranges = ranges.merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(datetime(1990, 2, 1), datetime(1990, 2, 27))])

    def test_merge_ranges_dt_with_none(self):
        list_of_ranges = [(None, datetime(1990, 2, 15)), (datetime(1990, 2, 15), None)]
        merged_ranges = ranges.merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, None)])


if __name__ == '__main__':
    unittest.main()
