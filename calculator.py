# -----------------------------------------------------------------------------
# calculator.py
# ----------------------------------------------------------------------------- 
"""
Before modification:
1044097 function calls (1042152 primitive calls) in 2.044 seconds

Function: hypotenuse at line 50
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    50                                           @profile
    51                                           def hypotenuse(x,y):
    52                                               
    53                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    54                                               x and y must be two-dimensional arrays of the same shape.
    55                                               
    56         1       768855 768855.0     25.7      xx = multiply(x,x)
    57         1       767200 767200.0     25.7      yy = multiply(y,y)
    58         1       789767 789767.0     26.4      zz = add(xx, yy)
    59         1       662928 662928.0     22.2      return sqrt(zz)
"""

"""
After modification:
44091 function calls (42146 primitive calls) in 0.185 seconds

Function: hypotenuse at line 57

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    57                                           @profile
    58                                           def hypotenuse(x,y):
    59                                               
    60                                               Return sqrt(x**2 + y**2) for two arrays, a and b.
    61                                               x and y must be two-dimensional arrays of the same shape.
    62                                               
    63         1         3454   3454.0     23.9      xx = multiply(x,x)
    64         1         3219   3219.0     22.3      yy = multiply(y,y)
    65         1         3230   3230.0     22.3      zz = add(xx, yy)
    66         1         4564   4564.0     31.5      return sqrt(zz)
"""

import numpy as np

def add(x,y):
    """
    Add two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    z=x+y
    return z


def multiply(x,y):
    """
    Multiply two arrays using a Python loop.
    x and y must be two-dimensional arrays of the same shape.
    """
    z=x*y
    return z


def sqrt(x):
    """
    Take the square root of the elements of an arrays using a Python loop.
    """
    z=np.sqrt(x)
    return z

@profile
def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = multiply(x,x)
    yy = multiply(y,y)
    zz = add(xx, yy)
    return sqrt(zz)