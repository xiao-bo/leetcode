from typing import (Optional, List)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Runtime: 92 ms, faster than 30.31% of Python3 online submissions for Kth Smallest Element in a BST.
        # Memory Usage: 18.1 MB, less than 44.27% of Python3 online submissions for Kth Smallest Element in a BST.
        self.ret = []
        self.inorder(root)
        
        return self.ret[k-1]

    def inorder(self, root):

        if root:
            self.inorder(root.left)
            self.ret.append(root.val)
            self.inorder(root.right)

