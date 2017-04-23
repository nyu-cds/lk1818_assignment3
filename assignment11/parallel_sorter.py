'''
Assignment 11
Author: Li Ke lk1818

This file can be executed directly to sort a large dataset using MPI.
'''

import numpy as np
from mpi4py import MPI 


def get_datasize():
	# This functions prompts the user for the size (an integer) of generated data. Returns wrong result if the input is not an integer.
	raw = input("Please enter an integer (at least 2) as data size:")
	try:
		data_size = int(raw)
	except ValueError:
		return

	return data_size

def generate_data():
	# This function generate a dataset of random elements, of the size entered by the user.
	data_size = get_datasize()
	while not isinstance(data_size, int): # Keeps prompting the user for an integer if the input is not an integer.
		print('Please input an integer')
		data_size = get_datasize()
	
	if data_size < 2: # If the size of dataset is too small (<2), it will be automatically set to 10000
		print('Input data size is too small to sort. Data size is now set to 10000.')
		data_size = 10000

	return np.random.randint(0, 1000, data_size)

def split(data, size):
	# This function splits the dataset into several equally-separated bins
	maxim = max(data)
	minim = min(data)
	bins = np.array_split(np.asarray(range(maxim+1)), size) # This array contains the start point and endpoint of each bin
	chunks = []
	for i in range(size):
		# Assign elements in the dataset into each bin according to its value
		chunks.append([x for x in data if (x in bins[i])])
	return chunks

def parallel_sort():
	# This function is an integeration.
	comm = MPI.COMM_WORLD
	rank = comm.Get_rank()
	size = comm.Get_size()

	if rank == 0:
		# Execute the following lines only if running on Processor 0 (Root)
		data = generate_data() # Generate data 
		chunks = split(data, size) # Split data into bins
	else:
		# If not running on Root, do nothing
		chunks = None 

	data_local = comm.scatter(chunks, root=0) # Scatter bins into different Processors
	data_local_sorted = np.sort(data_local) # Sort
	data_integrated = comm.gather(data_local_sorted, root=0) # Send bins back into Root, sorted

	if rank == 0:
		data_integrated_final = np.concatenate(data_integrated) # Merge all sorted bins into one sorted array


if __name__ == '__main__':
	parallel_sort()
