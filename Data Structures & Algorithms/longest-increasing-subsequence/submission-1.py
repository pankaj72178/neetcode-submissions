class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [[-1] * (n + 1) for _ in range(n)]

        def f(ind, prev_ind):

            if ind == n:
                return 0

            if dp[ind][prev_ind + 1] != -1:
                return dp[ind][prev_ind + 1]

            # Not take
            length = f(ind + 1, prev_ind)

            # Take
            if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                length = max(length, 1 + f(ind + 1, ind))

            dp[ind][prev_ind + 1] = length
            return length

        return f(0, -1)