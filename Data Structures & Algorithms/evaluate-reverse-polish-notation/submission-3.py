class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for k in range(len(tokens)):
            if tokens[k] not in ("+", "-", "*", "/"):
                stack.append(int(tokens[k]))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if tokens[k] == "+":
                    res = val2+val1
                    stack.append(res)
                if tokens[k] == "-":
                    res = val2-val1
                    stack.append(res)
                if tokens[k] == "*":
                    res = val2*val1
                    stack.append(res)
                if tokens[k] == "/":
                    res = int(val2/val1)
                    stack.append(res)

        return stack.pop()





        