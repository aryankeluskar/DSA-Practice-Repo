# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        root.left = TreeNode(preorder[1])
        # every value to the left of root in inorder is on left subtree, same for right
        rid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : rid + 1], inorder[:rid])
        root.right = self.buildTree(preorder[rid + 1 :], inorder[rid + 1 :])
        return root
