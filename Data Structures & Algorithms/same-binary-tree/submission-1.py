# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def issame(temp1,temp2):

            if not temp1 or not temp2:
                if (temp1 == temp2):
                    return True
                return False
            
            if(temp1.val != temp2.val):
                return False

            return issame(temp1.left,temp2.left) and issame(temp1.right,temp2.right)
        
        return issame(p,q)