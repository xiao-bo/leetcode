from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Postorder:
    def postorder(self, root: 'Node') -> List[int]:
        # using recursion method
        # Runtime: 50 ms, faster than 91.53% of Python3 online submissions for N-ary Tree Preorder Traversal.
        # Memory Usage: 16.4 MB, less than 13.77% of Python3 online submissions for N-ary Tree Preorder Traversal.
        
        stack = []
        if root.children:
            for children in root.children:
                stack.extend(self.postorder(children))

        if root:
            stack.append(root.val)

        return stack
        