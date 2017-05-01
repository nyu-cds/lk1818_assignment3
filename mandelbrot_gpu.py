#
# Simple Python program to calculate elements in the Mandelbrot set.
# Author: Li Ke
# lk1818


#
from numba import cuda
import numpy as np
from pylab import imshow, show

@cuda.jit(device=True)
def mandel(x, y, max_iters):
    '''
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the 
    Mandelbrot set given a fixed number of iterations.
    '''
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
            
    return max_iters
    

@cuda.jit
def compute_mandel(min_x, max_x, min_y, max_y, image, iters):
    '''
    Calculate the mandel value for each element in the 
    image array. The real and imag variables contain a 
    value for each element of the complex space defined 
    by the X and Y boundaries (min_x, max_x) and 
    (min_y, max_y).
    '''
    y,x = cuda.grid(2)

    height = image.shape[0]
    width = image.shape[1]

    x_end = cuda.blockDim.x * cuda.gridDim.x
    y_end = cuda.blockDim.y * cuda.gridDim.y
    
    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    index_length_x = int((width - y) / x_end)
    index_length_y = int((height - x) / y_end)
    for index_x in range(index_length_x):
        x_updated = y + index_x*x_end
        real = min_x + x_updated * pixel_size_x
        for index_y in range(index_length_y):
            y_updated = x + index_y*y_end
            imag = min_y + y_updated * pixel_size_y
            image[y_updated, x_updated] = mandel(real, imag, iters)
            
if __name__ == '__main__':
    image = np.zeros((1024, 1536), dtype = np.uint8)
    blockdim = (32, 8)
    griddim = (32, 16)
    
    image_global_mem = cuda.to_device(image)
    compute_mandel[griddim, blockdim](-2.0, 1.0, -1.0, 1.0, image_global_mem, 20) 
    image_global_mem.copy_to_host()
    imshow(image)
    show()