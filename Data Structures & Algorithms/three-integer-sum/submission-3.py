class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        lst =[]
        for i in range(len(snums)):
            left = i+1
            right = len(snums)-1
            while left<right:
                if -(snums[left]+snums[right])>snums[i]:
                    left+=1
                elif -(snums[left]+snums[right])<snums[i]:
                    right-=1
                elif -(snums[left]+snums[right])==snums[i]:
                    if [snums[i], snums[left], snums[right]] not in lst:
                        lst.append([snums[i], snums[left], snums[right]])
                    left+=1
                    right-=1

        return lst
