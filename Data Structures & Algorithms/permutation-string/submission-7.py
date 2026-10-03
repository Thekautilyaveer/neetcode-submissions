class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        for i in s1:
            count1[ord(i) - ord('a')] +=1

        start, end = 0, len(s1)
        for i in s2[0:len(s1)]:
            count2[ord(i) - ord('a')] +=1
            if count2 == count1:
                return True

        for end in range(len(s1), len(s2)):
            count2[ord(s2[end]) - ord('a')] +=1
            count2[ord(s2[end - len(s1)]) - ord('a')] -= 1
            if count2 == count1:
                return True
        return False      

                
        
