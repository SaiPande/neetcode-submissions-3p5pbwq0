class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        outputlist = len(arr)*[-1]
        print(outputlist) 
        for i in range(0, len(arr)-1):
            outputlist[i] = max(arr[i+1:])
        return outputlist        