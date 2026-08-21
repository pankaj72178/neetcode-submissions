class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [-1] * (target + 1)

        def possible(target):

            if target == 0:
                return 1

            if target < 0:
                return 0

            if dp[target] != -1:
                return dp[target]

            ways = 0

            for num in nums:
                ways += possible(target - num)

            dp[target] = ways
            return ways

        return possible(target)