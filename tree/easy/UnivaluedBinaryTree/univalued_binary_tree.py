from typing import List
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # Runtime: 56 ms, faster than 26.63% of Python3 online submissions for Univalued Binary Tree.
        # Memory Usage: 13.9 MB, less than 15.72% of Python3 online submissions for Univalued Binary Tree.
        root_val = root.val

        stack = [root]

        while stack:

            current = stack.pop()
            if current:
                if current.val != root_val:
                    return False

                if current.left:
                    stack.append(current.left)

                if current.right:
                    stack.append(current.right)

        return True
