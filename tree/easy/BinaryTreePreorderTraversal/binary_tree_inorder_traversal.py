from typing import List
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InorderTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []

        if root:
            if root.left:
                stack.extend(self.inorderTraversal(root.left))

            stack.append(root.val)

            if root.right:
                stack.extend(self.inorderTraversal(root.right))

        return stack
