class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        maxlen = 0
        numSet = set(nums)

        for val in nums:
            if val-1 not in numSet:
                length = 1
                while val+length in numSet:
                    length+=1
                maxlen = max( length, maxlen)
        return maxlen

                

        