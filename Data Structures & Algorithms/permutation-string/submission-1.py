class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        begin = 0
        end = len(s1)
        while end < len(s2)+1:
            if sorted(s2[begin:end]) != sorted(s1):
                begin +=1
                end +=1
            else:
                return True
        return False