class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        arr = []
        seen = set()

        for i in range(n):

            s = set()

            for j in range(i + 1, n):

                for k in range(j + 1, n):

                    need = target - (nums[i] + nums[j] + nums[k])

                    if need in s:

                        quad = sorted([
                            nums[i],
                            nums[j],
                            nums[k],
                            need
                        ])

                        if tuple(quad) not in seen:
                            seen.add(tuple(quad))
                            arr.append(quad)

                s.add(nums[j])

        return arr