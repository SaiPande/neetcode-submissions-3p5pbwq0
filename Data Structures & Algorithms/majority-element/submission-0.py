class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        target = len(nums)/2

        for i in nums:
            dict1[i] = dict1.get(i,0)+1

        for key, value in dict1.items():
            if value > target:
                return key
        return -1         