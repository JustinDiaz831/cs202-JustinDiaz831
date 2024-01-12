import unittest
from lab2 import max_list_iter, reverse_rec, bin_search

class TestLab2(unittest.TestCase):

    # Tests for max_list_iter
    def test_max_list_iter_custom1(self):
        self.assertEqual(max_list_iter([1000, 0, 92, -34, 400]), 1000)
        pass

    def test_max_list_iter_custom2(self):
        self.assertEqual(max_list_iter([-50, -34, 0]), 0)
        pass

    # Tests for reverse_rec
    def test_reverse_rec_custom1(self):
       self.assertEqual(reverse_rec([500, 23, 89, -10]), [-10, 89, 23, 500])
       pass

    def test_reverse_rec_custom2(self):
        self.assertEqual(reverse_rec([60]), [60])
        pass

    # Tests for bin_search
    def test_bin_search_custom1(self):
       self.assertIsNone(bin_search(8, 0, 4, [1, 2, 3, 4, 5]))
       pass

    def test_bin_search_custom2(self):
        self.assertEqual(bin_search(23, 0, 0, [23]), 0)
        pass

if __name__ == '__main__':
    unittest.main()
