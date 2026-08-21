class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def permutation(temp):

            if (len(temp)==len(nums)):
                ans.append(temp[:])
                return
            
            for num in nums:
                if(num in temp):
                    continue

                temp.append(num)
                permutation(temp)
                temp.pop()
        
        permutation([])

        return ans