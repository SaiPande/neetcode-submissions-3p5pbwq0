class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0
        #Boyer-Moore Voting Algorithm
        for i in nums:
            if count == 0:
                res = i
            if i == res:
                count += 1
            else:
                count -= 1    
            print('res')
            print(res)
            print('count')
            print(count)
        return res        