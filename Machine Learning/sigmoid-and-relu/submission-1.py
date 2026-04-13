import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        e = 2.71828
        output = []
        for i in z:
            output.append(round(1/(1+e**(-i)), 5))
        return output    
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        output = []
        for i in z:
            output.append(round(max(0.0,i),5))
        return output    
        pass
