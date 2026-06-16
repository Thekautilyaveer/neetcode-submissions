class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range (len(nums)):
            val = 1
            for j in nums[0:i]:
                val *=j
            for j in nums[i+1:]:
                val *=j
            output.append(int(val))

        return(output)
    
