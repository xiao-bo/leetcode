class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, current_node):
        if val < current_node.val:
            if current_node.left == None:
                current_node.left = TreeNode(val)
            else:
                self._insert(val, current_node.left)

        elif val > current_node.val:
            if current_node.right == None:
                current_node.right = TreeNode(val)
            else:
                self._insert(val, current_node.right)

        else:
            print('this value is existed')

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.val))
            self._print_tree(cur_node.right)


def findTarget(nums, target):
    bst = BinarySearchTree()
    for x in range(0, len(nums)):
        bst.insert(nums[x])

    bst.print_tree()


nums = [5, 3, 6, 2, 4, 1, 7]
findTarget(nums, 9)
