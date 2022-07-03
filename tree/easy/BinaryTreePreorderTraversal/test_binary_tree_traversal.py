from binary_tree_preorder_traversal import PreorderTraversal, TreeNode
from binary_tree_postorder_traversal import PostorderTraversal
from binary_tree_inorder_traversal import InorderTraversal


class TestTraversal(object):

    def setup(self):
        self.root1 = self._prepare_dataset_1()
        self.root2 = self._prepare_dataset_2()
        self.root3 = self._prepare_dataset_3()
        self.root4 = self._prepare_dataset_4()

    def _prepare_dataset_1(self):
        Node3 = TreeNode(3)
        Node2 = TreeNode(2, left=Node3, right=None)
        root = TreeNode(1, left=None, right=Node2)

        return root

    def _prepare_dataset_2(self):
        root = None
        return root

    def _prepare_dataset_3(self):
        root = TreeNode(1)
        return root

    def _prepare_dataset_4(self):
        Node6 = TreeNode(6)
        Node5 = TreeNode(5, right=Node6)
        Node4 = TreeNode(4)
        Node3 = TreeNode(3)
        Node2 = TreeNode(2, left=Node4, right=Node5)
        root = TreeNode(1, left=Node2, right=Node3)
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
