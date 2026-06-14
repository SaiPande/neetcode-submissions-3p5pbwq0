class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            elif bracket == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False   
            elif bracket == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False  
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False 
        if len(stack) > 0:
            return False
        return True                                

