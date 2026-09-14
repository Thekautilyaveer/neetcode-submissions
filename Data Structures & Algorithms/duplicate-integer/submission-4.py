class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snum = set(nums)
        if len(snum)<len(nums):
            return True
        else:
            return False