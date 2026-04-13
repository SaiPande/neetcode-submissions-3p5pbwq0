class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        outputlist = []
        for i in range(1, (len(nums)+1)):
            print(i)
            if i not in nums:
                outputlist.append(i)
        print(outputlist)        
        return outputlist        
