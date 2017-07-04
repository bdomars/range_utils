import unittest
from ranges import Range, merge_ranges, check_overlap

from datetime import datetime


class MergeTests(unittest.TestCase):

    def test_merge_ranges(self):
        list_of_ranges = [(2, 5), (3, 6), (8, 10)]
        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(2, 6), (8, 10)])

    def test_merge_ranges_with_none(self):
        list_of_ranges = [(None, 5), (3, 6), (8, None)]
        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, 6), (8, None)])

    def test_merge_ranges_unordered(self):
        list_of_ranges = [(2, 3), (1, 4), (7, 11), (6, 12)]
        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(1, 4), (6, 12)])

    def test_merge_ranges_unordered_with_none(self):
        list_of_ranges = [(2, 3), (None, 4), (7, None), (6, 12)]
        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, 4), (6, None)])

    def test_merge_ranges_empty(self):
        list_of_ranges = []
        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [])

    def test_merge_ranges_continuous(self):
        list_of_ranges = [(2, 6), (6, 9), (1, 2)]
        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(1, 9)])

    def test_merge_ranges_continuous_with_none(self):
        list_of_ranges = [(None, 2), (2, None), (6, 9)]
        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, None)])

    def test_merge_ranges_dt(self):
        list_of_ranges = [(datetime(1990, 2, 1), datetime(1990, 2, 15)), (datetime(1990, 2, 15), datetime(1990, 2, 27))]
        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(datetime(1990, 2, 1), datetime(1990, 2, 27))])

    def test_merge_ranges_dt_with_none(self):
        list_of_ranges = [(None, datetime(1990, 2, 15)), (datetime(1990, 2, 15), None)]
        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, None)])

    def test_merge_ranges_regression_1(self):
        list_of_ranges = [
            (None, datetime(2016, 3, 25)),
            (datetime(2016, 12, 19), datetime(2016, 12, 26)),
            (datetime(2016, 12, 8), datetime(2016, 12, 19)),
            (datetime(2016, 12, 26), datetime(2017, 1, 2)),
            (datetime(2017, 1, 2), datetime(2017, 4, 14)),
            (datetime(2016, 3, 28), datetime(2016, 11, 26)),
            (datetime(2016, 3, 25), datetime(2016, 3, 28)),
            (datetime(2016, 11, 26), datetime(2016, 12, 8)),
            (datetime(2017, 1, 1), None)
        ]

        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, None)])

    def test_merge_ranges_regression_2(self):
        list_of_ranges = [
            (datetime(2015, 12, 14), datetime(2015, 12, 24)),
            (datetime(2015, 12, 24), datetime(2016, 1, 3)),
            (datetime(2016, 1, 3), datetime(2016, 3, 25)),
            (datetime(2016, 3, 25), datetime(2016, 3, 29)),
            (datetime(2016, 3, 29), datetime(2016, 12, 11)),
            (datetime(2016, 12, 11), datetime(2016, 12, 25)),
            (datetime(2016, 12, 25), datetime(2017, 1, 2)),
            (datetime(2017, 1, 2), datetime(2017, 4, 14)),
            (datetime(2017, 4, 14), datetime(2017, 4, 20)),
            (datetime(2017, 4, 20), None),
            (None, datetime(2015, 12, 14)),
        ]

        merged_ranges = merge_ranges(list_of_ranges)
        self.assertEqual(merged_ranges, [(None, None)])


class OverlapTests(unittest.TestCase):

    def test_overlaps(self):
        self.assertTrue(check_overlap([(1, 4), (3, 6)]))
        self.assertTrue(check_overlap([(1, 4), (4, 6), (1, 5)]))
        self.assertTrue(check_overlap([(1, 4), (5, 8), (0, 3)]))

    def test_no_overlaps(self):
        self.assertFalse(check_overlap([(1, 4), (4, 8)]))
        self.assertFalse(check_overlap([(1, 4), (6, 9), (4, 6)]))

    def test_overlaps_with_none(self):
        self.assertTrue(check_overlap([(None, 4), (3, None)]))
        self.assertTrue(check_overlap([(1, 4), (None, 6), (1, None)]))
        self.assertTrue(check_overlap([(1, 4), (5, 8), (None, None)]))

    def test_no_overlaps_with_none(self):
        self.assertFalse(check_overlap([(None, 4), (4, None)]))
        self.assertFalse(check_overlap([(None, 4), (6, None), (4, 6)]))
        self.assertFalse(check_overlap([(None, None)]))


class ComparisonTests(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(Range(1, 1), Range(1, 1))
        self.assertEqual(Range(None, None), Range(None, None))

    def test_lt(self):
        self.assertLess(Range(None, None), Range(1, 3))
        self.assertLess(Range(1, 2), Range(1, 3))
        self.assertLess(Range(None, 5), Range(4, None))
        self.assertLess(Range(2, 5), Range(2, None))
        self.assertLess(Range(None, 5), Range(2, 5))
        self.assertLess(Range(3, 5), Range(4, None))
        self.assertLess(Range(3, 5), Range(3, None))


if __name__ == '__main__':
    unittest.main()
