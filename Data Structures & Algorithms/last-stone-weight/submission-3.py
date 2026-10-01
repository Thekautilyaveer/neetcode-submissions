class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStones = [-i for i in stones]
        heapq.heapify(maxStones)

        while len(maxStones) > 1:
            l1 = -heapq.heappop(maxStones)
            l2 = -heapq.heappop(maxStones)

            if l1 == l2:
                pass
            elif l1>l2:
                heapq.heappush(maxStones, -abs((l1-l2)))

            
        if len(maxStones) > 0:
            return -(maxStones[0])
        else:
            return 0