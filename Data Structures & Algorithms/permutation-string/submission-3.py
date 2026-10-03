class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {} 
        for i in s1: #a, d,c
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1
#hashmap = {a: 1, d:1, c:1}
        start, end = 0, len(s1)        
        while end <=len(s2):
            hashmap1 = {}
            for j in s2[start:end]:
                if j in hashmap1:
                    hashmap1[j] +=1
                else:
                    hashmap1[j] = 1
            if hashmap1 == hashmap:
                return True            
            start+=1
            end+=1
        return False
            


