class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []

        nums.sort()
       
        if nums[0] > 0:
            return []

        output = []

        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
                    
            j = i+1
            k = len(nums)-1    
            
            while j<k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum == 0:
                    output.append([nums[i],nums[j],nums[k]])
                    #to avoid duplicates
                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    while j<k and nums[k] == nums[k-1]:
                        k-=1    
                    j+=1
                    k-=1
                elif threesum > 0:
                    k-=1
                else:
                    j+=1  
        return output           
