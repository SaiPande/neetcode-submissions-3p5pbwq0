class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowedstr = set(allowed)
        for i in words:
            if set(i) <= allowedstr:
                count += 1
        return count        