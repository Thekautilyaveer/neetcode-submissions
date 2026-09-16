class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in mapp:
                return[mapp[comp]+1, i+1]
            mapp[numbers[i]] = i

        return 0
            