class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,j in enumerate(nums):
            compliment = target-j
            if compliment in seen:
                return[seen[compliment], i]
            else:
                seen[j] = i
            