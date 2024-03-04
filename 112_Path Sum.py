# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def inOrder(root, sum):
            if root:
                if not root.left and not root.right:
                    print(sum+root.val)
                    if sum+root.val == targetSum:
                        return True
            else:
                return False
            return inOrder(root.left, sum+root.val) or inOrder(root.right, sum+root.val)

        return inOrder(root,0)
