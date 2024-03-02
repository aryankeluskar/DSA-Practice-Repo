"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        md = 1
        if not root:
            return 0
        for i in root.children:
            curr = 1 + self.maxDepth(i)
            if curr > md:
                md = curr

        return md
        
