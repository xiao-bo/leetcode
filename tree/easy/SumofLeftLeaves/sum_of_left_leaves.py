from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.ret = 0
        self.get_sum(root, False)
        return self.ret


    def get_sum(self, root, is_left):
        ## Runtime: 65 ms, faster than 16.67% of Python3 online submissions for Sum of Left Leaves.
        ## Memory Usage: 14.7 MB, less than 45.73% of Python3 online submissions for Sum of Left Leaves.
        if root:
            if is_left and root.right is None and root.left is None:
                self.ret = self.ret + root.val
            else:
                self.get_sum(root.left, True)
                self.get_sum(root.right, False)
            
