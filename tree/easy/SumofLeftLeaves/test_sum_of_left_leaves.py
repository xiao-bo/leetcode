from SumofLeftLeaves.sum_of_left_leaves import Solution
from BinaryTree.build_binary_tree import binary_tree



class TestUnivaluedBinaryTree(object):

    def setup(self):
        self.root1 = binary_tree([1,None,2,3])
        self.root2 = binary_tree([1])
        self.root3 = binary_tree([1,2,3,4,5,None,None,None,None,None,6])
        self.root4 = binary_tree([3,9,20,None,None, 15,7])

    def test_s(self):
        s = Solution()


        assert s.sumOfLeftLeaves(self.root1) == 3


        assert s.sumOfLeftLeaves(self.root2) == 0


        assert s.sumOfLeftLeaves(self.root3) == 4


        assert s.sumOfLeftLeaves(self.root4) == 24


