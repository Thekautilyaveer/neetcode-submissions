class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        covered = []
        for i in range (len(strs)): 
            if strs[i] not in covered:               
                lst = [strs[i]]
                covered.append(strs[i])
                for j in range (i+1, len(strs)):
                    if ''.join(sorted(strs[i])) == ''.join(sorted(strs[j])):
                        lst.append(strs[j])
                        covered.append(strs[j])
                        
                final.append(lst)

        return final

