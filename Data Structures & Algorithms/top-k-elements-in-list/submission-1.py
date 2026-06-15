class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = set(nums)
        dict={}
        for i in s:
            temp = 0
            for j in nums:
                if i == j:
                    temp+=1
            dict[i] = temp


        keys = [k for k, v in sorted(dict.items(), key=lambda kv: kv[1], reverse=True)[:k]]
        return(keys) 





        