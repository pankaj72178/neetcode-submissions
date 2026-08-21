class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)

        if abs(target) > total:
            return 0

        if (target + total) % 2:
            return 0

        subset = (target + total) // 2

        dp = [0] * (subset + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset]