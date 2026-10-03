class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for word in strs:
            keys = [0] * 26
            for i in word:
                keys[ord(i)- ord('a')] +=1
            if tuple(keys) not in count:
                count[tuple(keys)] = [word]
            else:
                count[tuple(keys)].append(word)
        res = []
        for i in count.values():
            res.append(i)
        return res
        