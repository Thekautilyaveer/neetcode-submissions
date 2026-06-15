class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        x= []
        for i in s:
            x.append(i)
        for i in t:
            if i in x:
                x.remove(i)
            else:
                return False
        return True


        