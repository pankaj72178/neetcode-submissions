class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low<=high:
            if(high==0):
                if nums[0]==target:
                    return 0
                else:
                    return -1
            elif(high==1):
                if(nums[0]==target):
                    return 0
                elif(nums[1]==target):
                    return 1
                else:
                    return -1

            mid = low + (high-low)//2

            if(nums[mid]==target):
                return mid
            
            if(nums[low]<nums[mid]):
                if(nums[low]<=target<nums[mid]):
                    high = mid-1
                else:
                    low = mid+1
            else:
                if(nums[mid]<target<=nums[high]):
                    low = mid+1
                else:
                    high = mid-1
        return -1