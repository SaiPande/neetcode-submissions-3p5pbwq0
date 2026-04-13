class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in strs:
            srted = "".join(sorted(i))
            if srted in dict1:
                dict1[srted].append(i)
            else:
                dict1[srted] = [i]        

        return [v for v in dict1.values()]        