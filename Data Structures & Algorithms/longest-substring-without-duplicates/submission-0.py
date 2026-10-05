class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <1:
            return 0
        elif len(s) == 1:
            return 1
        else:        
            i = 0 
            j = 1
            maxset = 1
            windowset = set()
            windowset.add(s[i])
            while j<len(s):
                if s[j] not in windowset:
                    windowset.add(s[j])
                    j+=1  
                    maxset = max(maxset, j - i)
                else:
                    while s[j] in windowset:
                        windowset.remove(s[i])
                        i += 1
                    windowset.add(s[j])
                    j+=1    
        return maxset    

