import unittest
from merge import *

class TestMerge(unittest.TestCase):

    def test_merge(self):

        test_intervals = [[25,30], [2,19], [14, 23], [4,8]]
        
        merge_result = Merge.merge(intervals=test_intervals)

        self.assertEqual([[2,23], [25,30]], merge_result)


if __name__ == '__main__':
    unittest.main() 