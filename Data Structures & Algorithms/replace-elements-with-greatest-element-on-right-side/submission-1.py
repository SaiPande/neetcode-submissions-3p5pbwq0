class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        outputlist = len(arr)*[-1]
        newvar = -1
        for i in range(len(arr)-1, -1, -1):
            outputlist[i] = newvar
            newvar = max(arr[i],newvar)
        return outputlist    
