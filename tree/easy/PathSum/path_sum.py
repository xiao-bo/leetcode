from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ret = self._hasPathSum(root, targetSum)

        return ret

    def _hasPathSum(self, root, targetSum):
        # Runtime: 50 ms, faster than 81.57% of Python3 online submissions for Path Sum.
        # Memory Usage: 15.2 MB, less than 15.57% of Python3 online submissions for Path Sum.

        if root is None:
            return False

        # check node is leaf
        if self.__is_leaf(root, targetSum):
            return True

        ret = (
            self._hasPathSum(root.right, targetSum-root.val) |
            self._hasPathSum(root.left, targetSum-root.val)
        )
        return ret

    def __is_leaf(self, root, targetSum):
        return (
            not root.right and not root.left
            and root.val == targetSum
        )
