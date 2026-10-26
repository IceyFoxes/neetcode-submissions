class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list)
        self.userFollowers = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []

        for uid in self.userFollowers[userId] | {userId}:
            tweets = self.userTweets[uid]
            if tweets:
                index = len(tweets) - 1
                timestamp, tweetId = tweets[index]
                heap.append((-timestamp, tweetId, uid, index))

        heapq.heapify(heap)

        while len(feed) < 10 and heap:
            _, tweetId, uid, index = heapq.heappop(heap)
            feed.append(tweetId)

            if index > 0:
                index -= 1
                timestamp, tweetId = self.userTweets[uid][index]
                heapq.heappush(
                    heap, (-timestamp, tweetId, uid, index)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].discard(followeeId)
