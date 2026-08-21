class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums)
        total = sum(nums)

        curr_max = nums[0]
        max_sum = nums[0]
        curr_min = nums[0]
        min_sum = nums[0]

        for i in range(1,n):

            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum,curr_max)

            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)
        

        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)