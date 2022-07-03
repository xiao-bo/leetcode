from typing import List
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PreorderTraversal:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []

        if root:
            stack.append(root.val)

            if root.left:
                stack.extend(self.preorderTraversal(root.left))

            if root.right:
                stack.extend(self.preorderTraversal(root.right))

        return stack
