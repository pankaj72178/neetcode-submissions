class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        fun1(0,nums,subset,ans)
        return ans


def fun1(index,nums,subset,ans):
    if index==len(nums):
        ans.append(subset[:])
        return

    subset.append(nums[index])
    fun1(index+1,nums,subset,ans)
    subset.pop()
    fun1(index+1,nums,subset,ans)
    