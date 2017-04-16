'''
Assignment 10 Part 1
Author lk1818
April 16, 2017
'''


from mpi4py import MPI

# Create a communicator
comm = MPI.COMM_WORLD

# Get the rank of the calling process
rank = comm.Get_rank()

# check parity and print accordingly
if rank%2 == 0:
	print("Hello from process {}". format(rank))
else: 
	print("Goodbye from process {}".format(rank))

