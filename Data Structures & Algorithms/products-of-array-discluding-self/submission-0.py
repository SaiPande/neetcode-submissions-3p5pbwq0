class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mul = 1
        opt = []
        
        for i in range(len(nums)):
            mul = 1 
            for j in range(len(nums)):
                if i != j:
                    mul *= nums[j]
                   
            opt.append(mul)        

        return opt    