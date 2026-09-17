class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left<right:
            mid = (left+right)//2
            if nums[mid]>target:
                if right != mid:
                    right = mid
                else:
                    return -1
            elif nums[mid]<target:
                if left != mid:

                    left = mid
                else:
                    return -1
            else:
                return mid

        return -1

