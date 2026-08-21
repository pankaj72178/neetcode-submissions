class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        n = len(nums)

        dp = [[-1] * (target + 1) for _ in range(n)]

        def solve(idx, target):

            if target == 0:
                return True

            if idx == n:
                return False

            if dp[idx][target] != -1:
                return dp[idx][target]

            notTake = solve(idx + 1, target)

            take = False
            if nums[idx] <= target:
                take = solve(idx + 1, target - nums[idx])

            dp[idx][target] = take or notTake
            return dp[idx][target]

        return solve(0, target)