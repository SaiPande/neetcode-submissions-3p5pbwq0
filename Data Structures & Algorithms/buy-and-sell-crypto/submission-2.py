class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = i+1
        maxprofit = 0

        while i<j and j<=len(prices)-1:
            if prices[i] > prices[j]:
                i = j
            elif prices[i] < prices[j]:
                maxprofit = max(maxprofit, prices[j]-prices[i])
            j += 1    

        return maxprofit    
