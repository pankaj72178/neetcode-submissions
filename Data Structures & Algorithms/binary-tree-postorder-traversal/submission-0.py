# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def postorder(temp):
            if(temp):
                postorder(temp.left)
                postorder(temp.right)
                arr.append(temp.val)
        postorder(root)
        return arr