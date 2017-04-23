'''
Assignment 11
Author: Li Ke lk1818

This file is to test the split function from parallel_sorter module.
'''

import numpy as np
import unittest
from parallel_sorter import split

class TestSplit(unittest.TestCase):
	def set(self):
		pass

	def test_split(self): # This test case comes from the description of Assignment 11
		assert split([3,5,7,4,6,7,11,9,2,8,3,2], 4).tolist() = np.array([[2,2], [3,5,4,3], [7,6,7,8], [9, 11]]).tolist()  

if __name__ == '__main__':
	unittest.main()