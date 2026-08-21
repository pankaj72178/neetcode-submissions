class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        stack = []

        for i in range(len(tokens)):
            ch = tokens[i]


            if (ch == "+"):
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)

            elif (ch == "-"):
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            
            elif (ch == "*"):
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            
            elif (ch == "/"):
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            
            else:
                stack.append(int(ch))
        return stack[-1]