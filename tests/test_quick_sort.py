import unittest
from src.sorting.quickSort import quicksort

class TestQuickSort(unittest.TestCase):
    def test_sort_empty_list(self):
        self.assertEqual(quicksort([]), [])

    def test_sort_already_sorted_list(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sort_mixed_sign_list(self):
        self.assertEqual(quicksort([5, -3, 2, 0, -8, 4]), [-8, -3, 0, 2, 4, 5])

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestQuickSort))
