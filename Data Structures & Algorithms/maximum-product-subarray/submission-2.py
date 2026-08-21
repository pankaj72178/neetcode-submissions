class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxProd = nums[0]
        minProd = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            temp = maxProd

            maxProd = max(
                nums[i],
                nums[i] * maxProd,
                nums[i] * minProd
            )

            minProd = min(
                nums[i],
                nums[i] * temp,
                nums[i] * minProd
            )

            ans = max(ans, maxProd)

        return ans