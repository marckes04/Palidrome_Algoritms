import unittest
from src.sorting.heap import heapsort

class TestHeapSort(unittest.TestCase):
    def test_sort_empty_list(self):
        self.assertEqual(heapsort([]), [])

    def test_sort_already_sorted_list(self):
        self.assertEqual(heapsort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sort_random_list(self):
        self.assertEqual(heapsort([38, 27, 43, 3, 9, 82, 10]), [3, 9, 10, 27, 38, 43, 82])

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestHeapSort))

