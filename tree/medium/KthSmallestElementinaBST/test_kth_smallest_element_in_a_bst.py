
from BinaryTree.build_binary_tree import binary_tree, TreeNode, print_tree
from KthSmallestElementinaBST.kth_smallest_element_in_a_bst import (
    Solution)


class TestKthSmallestElementinaBST(object):

    def setup(self):
        self.root1 = binary_tree([3, 1, 4, None, 2])
        self.root2 = binary_tree([5, 3, 6, 2, 4, None, None, 1])
        self.root3 = binary_tree([60, 40, 100])

    def test_removeLeafNodes(self):

        s = Solution()

        assert s.kthSmallest(self.root1, 2) == 2
        assert s.kthSmallest(self.root1, 1) == 1
        assert s.kthSmallest(self.root1, 4) == 4

        assert s.kthSmallest(self.root2, 4) == 4
        assert s.kthSmallest(self.root2, 5) == 5
        assert s.kthSmallest(self.root2, 6) == 6

        assert s.kthSmallest(self.root3, 1) == 40
        assert s.kthSmallest(self.root3, 2) == 60
        assert s.kthSmallest(self.root3, 3) == 100
