class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxvol = 0

        while i<j:
            minwall = min(heights[i],heights[j])
            maxvol = max(maxvol,minwall*(j-i))
            if heights[i] == minwall:
                i+=1
            else:
                j-=1   
        return maxvol        
