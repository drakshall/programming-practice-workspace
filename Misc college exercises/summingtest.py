import unittest
from summinglist import *

class TestSummingList(unittest.TestCase):
    def test_can_construct_a_summing_list(self):
        #arrange
        sl = SummingList()

    def test_initial_sum_is_zero(self):
        # arrange
        sl = SummingList()
        # act
        # assert
        val = sl.get_total()
        self.assertEqual(val,0)

if __name__ == '__main__':
    unittest.main()

# first test, __inc_total missing 'self.'
