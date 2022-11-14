from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree(level_order: List) -> TreeNode:
    if not level_order:
        return None
    values = iter(level_order)
    root = TreeNode(next(values))
    nodes_to_fill = [root]
    try:
        while True:
            next_node = nodes_to_fill.pop(0)
            new_left = next(values)
            if new_left is not None:
                next_node.left = TreeNode(new_left)
                nodes_to_fill.append(next_node.left)
            new_right = next(values)
            if new_right is not None:
                next_node.right = TreeNode(new_right)
                nodes_to_fill.append(next_node.right)
    except StopIteration:
        return root

def print_tree(root):
    queue = [root]
    ret = []
    if not root:
        return []
    while queue:
        node = queue.pop(0)
        if node:
            ret.append(node.val)
        else:
            ret.append(None)
            continue
        if node.left:
            queue.append(node.left)
        else:
            queue.append(None)

        if node.right:
            queue.append(node.right)
        else:
            queue.append(None)

    for i in range(len(ret)-1, 0, -1):
        if ret[i] is None:
            ret.pop(i)
        else:
            break
    return ret


