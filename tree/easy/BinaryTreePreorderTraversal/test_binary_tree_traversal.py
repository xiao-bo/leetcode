from typing import List

from BinaryTreePreorderTraversal.binary_tree_preorder_traversal import PreorderTraversal, TreeNode
from BinaryTreePreorderTraversal.binary_tree_postorder_traversal import PostorderTraversal
from BinaryTreePreorderTraversal.binary_tree_inorder_traversal import InorderTraversal
from BinaryTree.build_binary_tree import binary_tree

class TestTraversal(object):

    def setup(self):
        self.root1 = binary_tree([1,None,2,3])
        self.root2 = binary_tree([])
        self.root3 = binary_tree([1])
        self.root4 = binary_tree([1,2,3,4,5,None,None,None,None,None,6])
        self.root5 = binary_tree([1,None, 2,3])

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
    