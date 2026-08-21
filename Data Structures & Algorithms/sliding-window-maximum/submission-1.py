class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mx = nums[0]
        ans = [0]*(len(nums)-k+1)

        for i in range(k):
            mx = max(mx,nums[i])
        
        for i in range(len(nums)-k):
            ans[i] = mx
            if (mx == nums[i]):
                mx = max(nums[i+1:i+k+1])
            mx = max(mx,nums[i+k])
        
        ans[-1] = max(mx,nums[-1])
        
        return ans