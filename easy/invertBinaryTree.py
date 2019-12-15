# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #Runtime: 20 ms, faster than 42.65% of Python online submissions for Invert Binary Tree.
        #Memory Usage: 11.8 MB, less than 62.50% of Python online submissions for Invert Binary Tree.

        tmp = None
        if root == None:
            return None
        else:
            
            tmp = root.right 
            root.right = root.left
            root.left = tmp 
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
    def printLVR(self,root):

        if root == None:
            return None
        else:

            self.printLVR(root.left)
            print(root.val)
        self.printLVR(root.right)


def main():
    root = TreeNode(2)

    ## level2 
    node1 = TreeNode(1)
    node3 = TreeNode(3)

    ## level3 
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    ## level 2
    root.left = node1
    root.right = node3

    ## level 3
    
    node1.left = node4
    node1.right = node5
    node3.left = node6 
    node3.right = node7
    
    a = Solution()
    a.printLVR(root)
    new = a.invertTree(root)
    print("==")
    a.printLVR(new)
    




if __name__ == '__main__':
    main()

