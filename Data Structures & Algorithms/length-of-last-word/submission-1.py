class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        lastword = 0
        for i in s[::-1]:
            if i == ' ' and flag == True:
                break
            if i != ' ':
                flag = True
                lastword += 1
        return lastword