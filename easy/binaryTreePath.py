class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ## iteration method
        ## dfs + stack
        ## Runtime: 16 ms, faster than 86.70% of Python online submissions for Binary Tree Paths.
        ## Memory Usage: 11.8 MB, less than 52.63% of Python online submissions for Binary Tree Paths.
        if not root:
            return []
        
        
        ans, stack = [],[(root,"")]
        #level = [root] if root else []
        while stack:
            node, ls= stack.pop()
            if not node.left and not node.right:
                ans.append(ls+str(node.val))
            if node.right:
                stack.append((node.right,ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left,ls+str(node.val)+"->"))

        
        print(ans)
        return ans
        
        '''

        ## recursion method
        ## Runtime: 16 ms, faster than 86.70% of Python online submissions for Binary Tree Paths.
        ## Memory Usage: 11.9 MB, less than 15.79% of Python online submissions for Binary Tree Paths.
        ans = []
        def dfs(root,route):
            if not root.left and not root.right:
                ## mean leaf
                ans.append(route)
            if root.left:
                dfs(root.left,route + "->" + str(root.left.val))
            if root.right:
                dfs(root.right,route + "->" + str(root.right.val))

        
        dfs(root,str(root.val))
        print(ans)
        '''

        
        


    def printLVR(self,root):

        if root == None:
            return None
        else:

            self.printLVR(root.left)
            print(root.val)
        self.printLVR(root.right)


def main():
    root = TreeNode(1)

    ## level2 
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    ## level3 
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    ## level4
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    ## level 2
    root.left = node2
    root.right = node3

    ## level 3
    
    node2.left = node4
    node2.right = node5
    node3.left = node6 
    node3.right = node7
    
    node5.left = node8
    node5.right = node9

    a = Solution()
    #a.printLVR(root)
    a.binaryTreePaths(root)
    #print("ans = {}".format(ans.val))
    
    
    




if __name__ == '__main__':
    main()
        