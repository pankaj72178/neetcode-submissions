class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        if(sum(nums)<target):
            return 0
        
        res = n
        for i in range(n):
            sm = 0
            for j in range(i,n):
                sm += nums[j]
                if (sm >= target):
                    res = min(res,j - i + 1)
                    break
        return res