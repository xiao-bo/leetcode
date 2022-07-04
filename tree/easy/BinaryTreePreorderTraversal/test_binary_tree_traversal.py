from typing import List

from binary_tree_preorder_traversal import PreorderTraversal, TreeNode
from binary_tree_postorder_traversal import PostorderTraversal
from binary_tree_inorder_traversal import InorderTraversal


class TestTraversal(object):

    def setup(self):
        self.root1 = self.binary_tree([1,None,2,3])
        self.root2 = self.binary_tree([])
        self.root3 = self.binary_tree([1])
        self.root4 = self.binary_tree([1,2,3,4,5,None,None,None,None,None,6])
        self.root5 = self.binary_tree([1,None, 2,3])
        
    def binary_tree(self, level_order: List) -> TreeNode:
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

    def test_preorder(self):
        preorder = PreorderTraversal()

        ret = preorder.preorderTraversal(self.root1)

        assert ret == [1, 2, 3]

        ret = preorder.preorderTraversal(self.root2)

        assert ret == []

        ret = preorder.preorderTraversal(self.root3)

        assert ret == [1]

        ret = preorder.preorderTraversal(self.root4)

        assert ret == [1, 2, 4, 5, 6, 3]

        ret = preorder.preorderTraversal(self.root5)
        assert ret == [1,2,3]
    
    def test_postorder(self):
        postorder = PostorderTraversal()

        ret = postorder.postorderTraversal(self.root1)

        assert ret == [3, 2, 1]

        ret = postorder.postorderTraversal(self.root2)

        assert ret == []

        ret = postorder.postorderTraversal(self.root3)

        assert ret == [1]

        ret = postorder.postorderTraversal(self.root4)

        assert ret == [4, 6, 5, 2, 3, 1]

    def test_inorder(self):
        inorder = InorderTraversal()

        ret = inorder.inorderTraversal(self.root1)

        assert ret == [1, 3, 2]

        ret = inorder.inorderTraversal(self.root2)

        assert ret == []

        ret = inorder.inorderTraversal(self.root3)

        assert ret == [1]

        ret = inorder.inorderTraversal(self.root4)

        assert ret == [4, 2, 5, 6, 1, 3]
    