import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}       # userId -> [(time, tweetId)]
        self.following = {}    # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:

        users = set()

        # Own tweets
        users.add(userId)

        # Followed users
        if userId in self.following:
            users.update(self.following[userId])

        heap = []

        for user in users:
            if user not in self.tweets:
                continue

            # Add all tweets of this user
            for time, tweetId in self.tweets[user]:
                heapq.heappush(heap, (-time, tweetId))

        ans = []

        while heap and len(ans) < 10:
            time, tweetId = heapq.heappop(heap)
            ans.append(tweetId)

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)