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
        
        
        #Runtime: 16 ms, faster than 74.14% of Python online submissions for Invert Binary Tree.
        #Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Invert Binary Tree.
        ## recursion method in 2022
        '''
        if root == None:
            return None
        else: 
            root.right,root.left = root.left, root.right
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
        '''

        ## iteration method in 2022
        ## Runtime: 12 ms, faster than 93.55% of Python online submissions for Invert Binary Tree.
        ## Memory Usage: 11.8 MB, less than 57.50% of Python online submissions for Invert Binary Tree.
        """
        stack = [root]
        
        
        while stack:
            node = stack.pop()
            if node:
                node.right,node.left = node.left, node.right
                stack.append(node.left)
                stack.append(node.right)
        return root
        """

        # recursion method in 2024 
        # Runtime 35ms Beats 57.69% of users with Python3
 i      # Memory 16.51MB Beats 37.39% of users with Python3
        if root is None:
            return root

        if root.left and root.right:
            # 左右都有值
            root.left, root.right = root.right, root.left
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)

        elif root.left and not root.right:
            root.right = root.left
            root.left = None
            root.right = self.invertTree(root.right)
        elif not root.left and root.right:
            root.left = root.right
            root.right = None
            root.left = self.invertTree(root.left)

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

