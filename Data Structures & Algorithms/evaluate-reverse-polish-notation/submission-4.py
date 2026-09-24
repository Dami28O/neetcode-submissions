class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = []

        for t in tokens:
            if t not in "+-*/":
                ops.append(int(t))
            else:
                # treat as an operand
                n1 = ops.pop(-1)
                n2 = ops.pop(-1)
                out = 1

                if t == "+":
                    out = n1 + n2
                elif t == "-":
                    out = n2 - n1
                elif t == "*":
                    out = n1 * n2
                else:
                    out = int(n2 / n1)
                
                ops.append(out)
        
        return ops[0]