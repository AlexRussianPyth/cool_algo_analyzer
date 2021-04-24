import numpy as np
import math



# This class makes calculations
class BigSlice:
    
    def __init__(self, range_begin, range_close):
        self.range = (range_begin, range_close)
        self.x_axis = np.linspace(self.range[0], self.range[1], num=20)

        # Make numpy array with rows as n's for our functions 

        constant_val = np.array([1 for i in range(len(self.x_axis))])
        linear_val = np.array([i for i in range(1, len(self.x_axis)+1)])
        quadratic_val = np.array([i**2 for i in range(1, len(self.x_axis)+1)])
        qubic_val = np.array([i**3 for i in range(1, len(self.x_axis)+1)])
        exp_val = np.array([2**i for i in range(1, len(self.x_axis)+1)])
        fact_val = np.array([math.factorial(i) for i in range(1, len(self.x_axis)+1)])
      
        self.func_array = np.vstack((constant_val,linear_val,quadratic_val,qubic_val, exp_val,fact_val))

