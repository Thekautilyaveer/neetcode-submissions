class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        val = self.data[key]
        i = 0
        j = len(val)-1
        res = ""
        while i<= j:
            mid = (i+j)//2
            if val[mid][0] > timestamp:
                j = mid-1
            elif val[mid][0] <= timestamp:
                res = val[mid][1]
                i = mid+1

        return res
            


        
