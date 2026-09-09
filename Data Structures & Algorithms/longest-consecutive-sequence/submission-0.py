class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestseq = 0
        seqset = set(nums)

        for i in nums:
            if i-1 in seqset:
                continue
            else:
                seqlen = 0
                t = i
                while t in seqset:
                    seqlen +=1
                    t+=1
                longestseq = max(longestseq, seqlen)
        return longestseq            
