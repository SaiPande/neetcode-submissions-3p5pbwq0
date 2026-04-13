import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        maxz = max(z)
        outputlist = []
        sum = 0
        for i in z:
            temp = (2.718)**(i-maxz)
            sum += temp
            outputlist.append(temp)

        return [round(k/sum, 4) for k in outputlist]  
