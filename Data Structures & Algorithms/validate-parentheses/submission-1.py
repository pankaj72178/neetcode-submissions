class Solution:
    def isValid(self, s: str) -> bool:

        o = {'(', '{', '['}
        stack = []

        for ch in s:
            
            if (ch in o):
                stack.append(ch)
            
            elif (ch == ')'):
                if(len(stack)==0):
                    return False
                else:
                    if(stack[-1] != '('):
                        return False
                    else:
                        stack.pop()
            
            elif (ch == '}'):
                if(len(stack)==0):
                    return False
                else:
                    if(stack[-1] != '{'):
                        return False
                    else:
                        stack.pop()
            
            elif (ch == ']'):
                if(len(stack)==0):
                    return False
                else:
                    if(stack[-1] != '['):
                        return False
                    else:
                        stack.pop()
            
        if(len(stack)==0):
            return True

        return False
            