class Solution:
    def maxPathSum(self, root):
        ans = float('-inf')

        def dfs(root):
            nonlocal ans
            if root is None:
                return 0
            
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))

            ans = max(ans,root.val + left + right)

            return root.val + max(left,right)
        
        dfs(root)
        return ans