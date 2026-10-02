class Solution:
    def isValid(self, s: str) -> bool:
        vals = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in ['(', '{', '[']:

                stack.append(i)

            elif i in [')', '}', ']']:
                if stack == []:
                    return False
                k = stack.pop()
                if vals[k] != i:
                    return False

        if stack == []: return True 
        else: return False


        
        