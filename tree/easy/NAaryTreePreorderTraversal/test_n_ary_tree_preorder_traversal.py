from n_ary_tree_preorder_traversal import (Preorder, Node)
from n_ary_tree_postorder_traversal import (Postorder, Node)


class TestSolution(object):

    def setup(self):
        self.root1 = self._prepare_dataset_1()
        self.root2 = self._prepare_dataset_2()

    def _prepare_dataset_1(self):

        values = [1, None, 3, 2, 4, None, 5, 6]
        stack = []
        root = Node(values.pop(0))

        node6 = Node(6)
        node5 = Node(5)
        node4 = Node(4)
        node3 = Node(2)
        node2 = Node(3, [node5, node6])
        root = Node(1, [node2, node3, node4])
        return root

    def _prepare_dataset_2(self):
        values = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None,
                  9, 10, None, None, 11, None, 12, None, 13, None, None, 14]

        node14 = Node(14)
        node13 = Node(13)
        node12 = Node(12)
        node11 = Node(11, [node14])
        node10 = Node(10)
        node9 = Node(9, [node13])
        node8 = Node(8, [node12])
        node7 = Node(7, [node11])
        node6 = Node(6)
        node5 = Node(5, [node9, node10])
        node4 = Node(4, [node8])
        node3 = Node(3, [node6, node7])
        node2 = Node(2)
        root = Node(1, [node2, node3, node4, node5])
        return root

    def test_preorder(self):
        self.preorder = Preorder()
        root = self._prepare_dataset_1()
        ret = self.preorder.preorder(self.root1)

        assert ret == [1, 3, 5, 6, 2, 4]

        root = self._prepare_dataset_2()
        ret = self.preorder.preorder(self.root2)

        assert ret == [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]

    def test_postorder(self):
        self.postorder = Postorder()

        root = self._prepare_dataset_1()
        ret = self.postorder.postorder(self.root1)

        assert ret == [5, 6, 3, 2, 4, 1]

        root = self._prepare_dataset_2()
        ret = self.postorder.postorder(self.root2)

        assert ret == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
