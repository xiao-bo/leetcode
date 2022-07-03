from typing import List
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PostorderTraversal:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []

        if root:
            if root.left:
                stack.extend(self.postorderTraversal(root.left))

            if root.right:
                stack.extend(self.postorderTraversal(root.right))

            stack.append(root.val)

        return stack
