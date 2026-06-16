class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        max = 1
        for i in range(len(s)):
            
            subs = []
            n = 0
            while (i + n) < len(s) and s[i+n] not in subs:
                subs.append(s[i+n])
                n+=1

                if len(subs)>max:
                    max = len(subs)

        return max
        