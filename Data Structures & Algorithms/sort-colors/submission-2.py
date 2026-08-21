class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)  
        arr = [0]*3
        for i in range(n):
            arr[nums[i]]+=1

        for i in range(n):
            if(i<arr[0]):
                nums[i] = 0
            elif(i<arr[0]+arr[1]):
                nums[i] = 1
            else:
                nums[i] = 2