from _heapq import heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        has = {}
        vals = []
        for item in points:
            x1, y1 = item
            dist = ((x1)**2 + (y1)**2)**0.5
            vals.append([-dist, x1, y1])
        
        heapq.heapify(vals)

        for item in vals:
            while len(vals) > k:
                heapq.heappop(vals)
        vals = [items[1:] for items in vals]
        return vals

        

        