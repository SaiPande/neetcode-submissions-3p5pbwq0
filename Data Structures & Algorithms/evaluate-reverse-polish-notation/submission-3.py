class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        def add(x,y): return x+y
        def subtract(x,y): return x-y
        def multiply(x,y): return x*y
        def divide(x,y): return int(x/y)

        operations = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide
        }

        for i in tokens:
            if i in '+-*/' and stk:
                b = stk.pop()
                a = stk.pop()
                stk.append(operations[i](a,b))
            else:
                stk.append(int(i))   
        return stk[-1]            