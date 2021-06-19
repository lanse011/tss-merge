import unittest
from merge import Merge

class TestMerge(unittest.TestCase):

    """ Test merge with valid data"""
    def test_merge(self):

        test_intervals = [[25,30], [2,19], [14, 23], [4,8]]
        
        merge_result = Merge.merge(intervals=test_intervals)

        self.assertEqual([[2,23], [25,30]], merge_result)


    """ Test merge with an interval that has 3 values instead of 2"""
    def test_merge_with_wrong_interval_input1(self):

        test_intervals = [[25, 30, 40], [2,19], [14, 23], [4,8]]

        merge_result = Merge.merge(intervals=test_intervals)

        self.assertEqual("'[25, 30, 40]' is not an interval", merge_result)


    """ Test merge with a character instead of numbers"""
    def test_merge_with_wrong_interval_input2(self):

        test_intervals = ['A', [2,19], [14, 23], [4,8]]

        merge_result = Merge.merge(intervals=test_intervals)

        self.assertEqual("'A' is not an interval", merge_result)


    """ Test merge with empty intervals list """
    def test_merge_with_empty_interval_input(self):

        test_intervals = []

        merge_result = Merge.merge(intervals=test_intervals)

        self.assertEqual([], merge_result)


if __name__ == '__main__':
    unittest.main() 