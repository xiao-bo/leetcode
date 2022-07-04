from PathSum.path_sum import Solution
from BinaryTree.build_binary_tree import binary_tree, TreeNode



class TestPathSum(object):

    def setup(self):
        self.root1 = binary_tree([1,None,2,3])
        self.root2 = binary_tree([])
        self.root3 = binary_tree([1])
        self.root4 = binary_tree([1,2,3,4,5,None,None,None,None,None,6])
        self.root5 = binary_tree([11,-11,None,11])

    def test_preorder(self):
        path_sum = Solution()

        assert path_sum.hasPathSum(self.root1, 3) == False

        assert path_sum.hasPathSum(self.root1, 6) == True

        assert path_sum.hasPathSum(self.root2, 0) == False

        assert path_sum.hasPathSum(self.root3, 1) == True

        assert path_sum.hasPathSum(self.root4, 7) == True
        assert path_sum.hasPathSum(self.root4, 4) == True
        assert path_sum.hasPathSum(self.root4, 8) == False
        assert path_sum.hasPathSum(self.root4, 14) == True

        assert path_sum.hasPathSum(self.root5, 11) == True
