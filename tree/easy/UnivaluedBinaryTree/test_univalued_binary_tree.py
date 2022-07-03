from univalued_binary_tree import Solution, TreeNode


class TestUnivaluedBinaryTree(object):

    def setup(self):
        self.root1 = self._prepare_dataset_1()
        self.root2 = self._prepare_dataset_2()
        self.root3 = self._prepare_dataset_3()


    def _prepare_dataset_1(self):
        Node3 = TreeNode(1)
        Node2 = TreeNode(1, left=Node3, right=None)
        root = TreeNode(1, left=None, right=Node2)

        return root

    def _prepare_dataset_2(self):
        root = TreeNode(1)
        return root

    def _prepare_dataset_3(self):
        Node6 = TreeNode(1)
        Node5 = TreeNode(1, right=Node6)
        Node4 = TreeNode(2)
        Node3 = TreeNode(1)
        Node2 = TreeNode(1, left=Node4, right=Node5)
        root = TreeNode(1, left=Node2, right=Node3)
        return root

    def test_s(self):
        s = Solution()
        
        ret = s.isUnivalTree(self.root1)

        assert ret == True

        ret = s.isUnivalTree(self.root2)

        assert ret == True
        
        ret = s.isUnivalTree(self.root3)

        assert ret == False
