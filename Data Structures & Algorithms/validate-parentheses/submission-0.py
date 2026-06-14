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
                    stack.append(bracket)    
            elif bracket == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(bracket)  
            else:
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(bracket) 
        if len(stack) > 0:
            return False
        return True                                

