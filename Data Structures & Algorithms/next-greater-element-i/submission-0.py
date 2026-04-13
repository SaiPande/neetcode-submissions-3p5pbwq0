class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #monotonic stack

        monotonicstack = []
        outputlist = []

        for i in nums1:
            idx = nums2.index(i)
            j = idx+1
            gn = -1
            while j < len(nums2):
                if nums2[idx] < nums2[j]:
                    gn = nums2[j]
                    break
                j+= 1    
            outputlist.append(gn)

        return outputlist            

                   

