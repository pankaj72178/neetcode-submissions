class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        n = len(nums)
        nums.sort()
        s = set()

        for i in range(n):
            for j in range(i+1,n):
                if(-nums[i]-nums[j] in s):
                    arr.append([-nums[i]-nums[j],nums[i],nums[j]])
            s.add(nums[i])
        t = set(tuple(x) for x in arr)

        result = [list(x) for x in t]
        return result