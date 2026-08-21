# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)

        def insert(temp,val):

            if (temp.val > val):
                if (temp.left is None):
                    temp.left = TreeNode(val)
                    return
                else:
                    insert(temp.left,val)
            
            else:
                if (temp.right is None):
                    temp.right = TreeNode(val)
                    return
                else:
                    insert(temp.right,val)
        insert(root,val)
        return root