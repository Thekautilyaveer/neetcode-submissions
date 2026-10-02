class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time+=1


    def getNewsFeed(self, userId: int) -> list[int]:
        self.following[userId].add(userId)
        heap = []
        for user in self.following[userId]:

            for i in self.tweets[user][-10:]:
                

                t, tweetId = i
                heap.append((-t, tweetId))

        heapq.heapify(heap)

        res = []
        while heap and len(res)<10:
            t, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId) 
        

