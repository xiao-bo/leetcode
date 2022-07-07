from DeleteLeavesWithaGivenValue.delete_leaves_with_a_given_value import (
    Solution)
from BinaryTree.build_binary_tree import binary_tree, TreeNode, print_tree


class TestDeleteLeavesWithaGivenValue(object):

    def setup(self):
        self.root1 = binary_tree([1, 2, 3, 2, None, 2, 4])
        self.root2 = binary_tree([1, 3, 3, 3, 2])
        self.root3 = binary_tree([1, 2, None, 2, None, 2])

    def test_removeLeafNodes(self):

        s = Solution()
        return_tree = s.removeLeafNodes(self.root1, 2)
        ret = print_tree(return_tree)

        assert ret == [1, None, 3, None, 4]

        return_tree = s.removeLeafNodes(self.root2, 3)
        ret = print_tree(return_tree)

        assert ret == [1, 3, None, None, 2]

        return_tree = s.removeLeafNodes(self.root3, 2)
        ret = print_tree(return_tree)

        assert ret == [1]
