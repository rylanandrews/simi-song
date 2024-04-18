# Author(s): Rylan Andrews

# Testing instructions:
#   run python -m unittest -v unit_tests.py
  
import src.shell_sort as shell_sort

import unittest

class TestSortMethods(unittest.TestCase):

    def test_shellsort_simple(self):
        sampleList = [
            ["song5", 5],
            ["song3", 3],
            ["song6", 6],
            ["song1", 1],
            ["song3", 3],
            ["song8", 8],
        ]

        sortedList = [
            ["song8", 8],
            ["song6", 6],
            ["song5", 5],
            ["song3", 3],
            ["song3", 3],
            ["song1", 1],
        ]

        self.assertEqual(shell_sort.shell_sort(sampleList), sortedList)

    def test_shellsort_moreSongs(self):
        sampleList = [
            ["song5", 5],
            ["song3", 3],
            ["song6", 6],
            ["song1", 1],
            ["song3", 3],
            ["song8", 8],
            ["song10", 10],
            ["song9", 9],
        ]

        sortedList = [
            ["song10", 10],
            ["song9", 9],
            ["song8", 8],
            ["song6", 6],
            ["song5", 5],
            ["song3", 3],
            ["song3", 3],
            ["song1", 1],
        ]

        self.assertEqual(shell_sort.shell_sort(sampleList), sortedList)

if __name__ == '__main__':
    unittest.main()