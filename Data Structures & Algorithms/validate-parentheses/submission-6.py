class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2 or len(s) % 2 != 0:
            return False
            
        opened = ('(', '{', '[')
        closed = {')': '(', 
                '}': '{',
                ']':'['}

        stack = []

        for c in s:
            if c in opened:
                stack.append(c)
            else:
                # compare it to the earliest entry in the stack
                if len(stack) > 0 and stack[-1] != closed[c]:
                    return False
                elif len(stack) > 0:
                    stack.pop(-1)
                else:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True