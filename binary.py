"""
Assitnment 5 Advanced Python
Author: lk1818
Date: 02/26/2017
"""

import itertools

def zbits(n, k):
	"""
	This function two two arguments n, k, and prints all binary strings of length n that contain k zero bits, one per line. 
	This logic of this function is as follows:

	1. Create a string of length k, filled with "0"s.
	2. Create a string of length (n-k), filled with "1"s.
	3. Concatenate these two strings.
	4. Iterate through all the permutations of the concatenated string, and print them. 
	"""


	## Create a string of length k, filled with "0"s
	zeros = "0"*k

	## Create a string of length (n-k), filled with "1"s
	ones = "1"*(n-k)

	## Concatenate these two strings
	new = zeros + ones

	## Now iterate through all the possible permutations (of length n) of the concatenated string, and print them
	## Making the permutations into a set automatically deletes out the redundant elements, and keeps only the unique values
	new_list = list()
	all_sets = set(itertools.permutations(new, n))
	for list_of_zero_one in all_sets:
		new_list.append(''.join(list_of_zero_one))


	## Return a set as prompted in the assignment
	new_set = set(new_list)


	return new_set


if __name__ == '__main__':
	## Test if the function returns correct results. If not, assertion errors will rise.
	assert zbits(4, 3) == {'0100', '0001', '0010', '1000'}
	assert zbits(4, 1) == {'0111', '1011', '1101', '1110'}
	assert zbits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}



