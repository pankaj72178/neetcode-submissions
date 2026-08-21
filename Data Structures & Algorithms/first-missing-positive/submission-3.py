class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(nums)
        for i in range(1,n+1):
            if i not in s:
                return i
        return n+1