class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = defaultdict(int)
        for n in range(len(nums)):
            needed = target - nums[n]
            if needed in mapp.keys():
                if mapp[needed] > n:
                    return [n, mapp[needed]]
                else:
                    return [ mapp[needed], n]
            mapp[nums[n]] = n


            
        



#Loop through twice: compare every number to every other number (O(n^2))
#save it in a list as seen, when we encounter it, we know it exists in the array, traverse again to find the index -> O(n^2))
#Hash map: {number : index}