class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []


        def dfs(subset, index):
            if index == len(nums):
                res.append(subset[:])
                return

            subset2 = subset.copy()
            subset2.append(nums[index])
            dfs(subset2, index+1)
            subset2.pop()
            while index+1 < len(nums) and nums[index+1] == nums[index]:
                index = index+1
            dfs(subset2, index+1)


        

        nums.sort()

        dfs(subset, 0)
        return res