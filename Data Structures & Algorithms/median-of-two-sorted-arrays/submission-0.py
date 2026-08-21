class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        nums3 = []
        i,j=0,0

        while i<n1 and j<n2:
            if(nums1[i]>nums2[j]):
                nums3.append(nums2[j])
                j+=1
            else:
                nums3.append(nums1[i])
                i+=1
        
        while i<n1:
            nums3.append(nums1[i])
            i+=1

        while j<n2:
            nums3.append(nums2[j])
            j+=1

        t = (n1+n2)//2
        if((n1+n2)%2==0):
            return (nums3[t]+nums3[t-1])/2
        return nums3[t]