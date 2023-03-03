import unittest
from src.sorting.merge import mergeSort

class TestMergeSort(unittest.TestCase):
    def test_sort_single_item_list(self):
        self.assertEqual(mergeSort([5]), [5])

    def test_sort_reverse_order_list(self):
        self.assertEqual(mergeSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sort_duplicate_items_list(self):
        self.assertEqual(mergeSort([1, 4, 2, 4, 1, 2]), [1, 1, 2, 2, 4, 4])

if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMergeSort))