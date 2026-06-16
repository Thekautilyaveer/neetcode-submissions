class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mmaxx = 0
        
        for i in nums:
            maxx = 1
            n = 1
            while (i+n) in nums:
               maxx +=1
               n+=1
            
            if maxx > mmaxx:
                mmaxx = maxx
        
        return mmaxx
        