# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def preorder(temp):
            if(temp):
                arr.append(temp.val)

                preorder(temp.left)
                preorder(temp.right)
        preorder(root)
        return arr