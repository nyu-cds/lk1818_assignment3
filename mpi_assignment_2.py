'''
Assignment 10 Part 2
Author lk1818
April 16, 2017
'''

import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

randNum = np.zeros(1)

if rank == 0:
	# Prompt for the raw input 
	raw = input('Please type in an integer between 0 and 100.')
	# Check if the raw input can be converted to an integer
	try:
		value = int(raw)
	except ValueError:
		print('Wrong type of input. Please type in an integer between 0 and 100.')
		value = 0

	# Check if the input integer is between 0 and 100
	if value < 0 or value > 100:
		raise ValueError
		print('Input integer out of range. Please type in an integer between 0 and 100.')
		value = 0

	randNum[0] = value
	# Sends the number to Process 1
	print('Process', rank, 'received the number', randNum[0])
	req = comm.Isend(randNum, dest=rank+1)
	print('Process', rank, 'sent the number', randNum[0])

else:
	# Receive value from previous process
	req = comm.Irecv(randNum, source=rank-1)
	req.Wait()
	print('Process', rank, 'received the number', randNum[0])

	# Send the number multiplied by rank of this Process to the next process
	randNum[0] = randNum[0] * rank
	if rank < size:
		comm.Isend(randNum, dest=rank+1)
	else:
		comm.Isend(randNum, dest=0)
	print('Process', rank, 'sent the number', randNum[0])
