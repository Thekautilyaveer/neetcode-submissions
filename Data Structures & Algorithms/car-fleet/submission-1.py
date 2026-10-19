class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        i = 0
        while i<len(position):
            pairs.append([position[i], speed[i]])
            i+=1
        pairs.sort()

        fleets = 1
        stack = []
        for i in range(len(pairs)-1, -1, -1):
            remaining_time = (target - pairs[i][0])/pairs[i][1]
            if stack == []:
                stack.append(remaining_time)
            while stack and remaining_time > stack[-1]:
                fleets+=1
            
                stack.append(remaining_time)

        return fleets


        