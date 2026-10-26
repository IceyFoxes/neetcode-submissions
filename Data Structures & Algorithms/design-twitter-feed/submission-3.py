class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list)
        self.userFollowers = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = heapq.nlargest(10, self.userTweets[userId])
        heapq.heapify(heap)
        
        for followeeId in self.userFollowers[userId]:
            for tweet in self.userTweets[followeeId]:
                if len(heap) >= 10:
                    heapq.heappushpop(heap, tweet)
                else:
                    heapq.heappush(heap, tweet)
        
        heap.sort(reverse=True)
        return [tweetId for _, tweetId in heap]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].discard(followeeId)
