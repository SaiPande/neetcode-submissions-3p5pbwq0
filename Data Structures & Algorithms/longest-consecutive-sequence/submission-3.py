class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            longestseq = 1
            setnum = set(nums)

            for i in range(len(nums)):
                if nums[i]-1 in setnum:
                    continue
                else:
                    cnt = 1
                    j = nums[i]+1
                    while j in setnum:
                        cnt +=1
                        longestseq = max(longestseq, cnt)
                        j+=1
            return longestseq                