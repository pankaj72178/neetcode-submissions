class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        t = 1
        for i in range(1,len(nums)):
            if(t==0):
                maj = nums[i]
                t+=1
            elif(nums[i]==maj):
                t+=1
            elif(nums[i]!=maj):
                t-=1
        return maj