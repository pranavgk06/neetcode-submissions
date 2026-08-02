class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        arr = []
        min_heap = []
        self.followMap[userId].add(userId)
        for fId in self.followMap[userId]:
            if fId in self.tweetMap:
                index = len(self.tweetMap[fId]) - 1
                count, tweetId = self.tweetMap[fId][index]
                heapq.heappush(min_heap, [count, tweetId, fId, index - 1])
        while min_heap and len(arr) < 10:
            count, tweetId, fId, index = heapq.heappop(min_heap)
            arr.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[fId][index]
                heapq.heappush(min_heap, [count, tweetId, fId, index - 1])
        return arr
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)