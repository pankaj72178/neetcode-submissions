class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if len(nums)<k:
            return False
        
        if len(nums)==k:
            for i in range(1,k):
                if(nums[i]!=nums[i-1]):
                    return False
            return True
        
        sm = sum(nums)
        mx = max(nums)

        if( sm%k != 0):
            return False

        if( k*mx > sm):
            return False
        
        t = sm//k

        nums.sort(reverse=True)

        sides = [0] * k

        def backtrack(index):
            if index == len(nums):
                return all(side == t for side in sides)

            for i in range(k):
                if sides[i] + nums[index] <= t:
                    sides[i] += nums[index]

                    if backtrack(index + 1):
                        return True

                    sides[i] -= nums[index]

                if sides[i] == 0:
                    break

            return False

        return backtrack(0)