class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if(n==1):
            return nums[0]
        if(n==2):
            return max(nums)
        
        arr = [0]*n

        arr[0] = nums[0]
        arr[1] = nums[1]

        mx = nums[0]

        for i in range(2,n):
            arr[i] = nums[i] + mx
            mx = max(mx,arr[i-1])

        return max(arr[-1],arr[-2])