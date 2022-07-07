from typing import (Optional, List)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Runtime: 75 ms, faster than 57.45% of Python3 online submissions for Delete Leaves With a Given Value.
        # Memory Usage: 14.6 MB, less than 88.64% of Python3 online submissions for Delete Leaves With a Given Value.

        if self._remove_leaf(root, target):
            return None

        return root

    def _remove_leaf(self, root, target):

        if not root:
            return False

        #print(f'root = {root.val}')

        if self._is_leaf(root) == False:
            #print(f'{root.val} is not leaf')
            if self._remove_leaf(root.left, target):
                #print(f"root.left = {root.left.val} is leaf, so remove")
                root.left = None
            if self._remove_leaf(root.right, target):
                #print(f"root.right = {root.right.val} is leaf, so remove")

                root.right = None

        if self._is_leaf(root) and root.val == target:
            #print(f'找到leaf, root.val = {root.val}')
            return True

    def _is_leaf(self, root):
        if root.right or root.left:
            return False

        else:
            return True