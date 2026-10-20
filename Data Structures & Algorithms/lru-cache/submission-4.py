class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.q = deque()


    def get(self, key: int) -> int:
        if key in self.data:
            self.q.remove(key)
            self.q.append(key)
            return self.data[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.data: 
            self.q.remove(key)
            self.q.append(key)
            self.data[key]= value
        else:
            if len(self.data) >= self.capacity:
                val = self.q.popleft()
                del self.data[val]
            self.q.append(key)
            self.data[key]= value
