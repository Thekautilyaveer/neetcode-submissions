class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        freq = [-i for i in counts.values()]
        heapq.heapify(freq)

        q = collections.deque()
        time = 0
        while q or freq:

            if q:
                if q[0][1] == time:
                    
                    heapq.heappush(freq, q[0][0])
                    q.popleft()
            if freq:
                val = heapq.heappop(freq)
                if (val+1) < 0:
                    q.append([(val+1), time+n+1])

            time+=1

        return time





        