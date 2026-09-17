class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        begin = 0
        end = k
        vals =[]
        heap = []
        if k>len(nums):
            vals.append(nums)
            return vals 
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i>(k-2):
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                vals.append(-heap[0][0])

        return vals

        