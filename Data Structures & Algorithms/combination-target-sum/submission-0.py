class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []

        def backtrack(start, remaining, temp):
            if remaining == 0:
                ans.append(temp[:])      # copy!
                return
            if remaining < 0:
                return
            for i in range(start, len(nums)):
                temp.append(nums[i])
                # pass i (not i+1) because the same element can be reused
                backtrack(i, remaining - nums[i], temp)
                temp.pop()               # backtrack!

        backtrack(0, target, [])
        return ans