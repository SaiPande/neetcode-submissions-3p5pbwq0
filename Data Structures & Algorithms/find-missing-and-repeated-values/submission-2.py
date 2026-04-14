class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        optlist = []
        n = len(grid)*len(grid)
        for i in grid:
            for j in i:
                optlist.append(j)
        
        total = (n*(n+1))//2
        actualsum = sum(optlist)
        twice = total - actualsum
        missing = 0
        for i in range(1, n+1):
            if i not in optlist:
                missing = i
        if twice > 0:
            twice = missing - twice        
        if twice < 0:
            twice = (twice*(-1))+ missing
            
        return [twice, missing]
       


        
           
                   