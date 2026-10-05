class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        res = []
        def dfs(arr, index):

            if index == len(nums):
                res.append(arr[:])
                return
            
            arr2 = arr.copy()
            dfs(arr2, index+1)
            arr2.append(nums[index])
            dfs(arr2, index+1)
            arr2.pop()


            
            



        dfs(subsets, 0)
        return res






        
        