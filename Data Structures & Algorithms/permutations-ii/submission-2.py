class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        used = [False]*len(nums)

        def backtrack(temp):

            if(len(temp)==len(nums)):

                if(temp not in ans):
                    ans.append(temp[:])
                return
            
            for i in range(len(nums)):

                if used[i]:
                    continue

                # Skip duplicate permutations
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                temp.append(nums[i])

                backtrack(temp)

                temp.pop()
                used[i] = False

        backtrack([])
        return ans
        