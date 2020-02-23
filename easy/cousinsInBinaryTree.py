# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        ## Runtime: 20 ms, faster than 69.80% of Python online submissions for Cousins in Binary Tree.
        ## Memory Usage: 11.9 MB, less than 58.33% of Python online submissions for Cousins in Binary Tree.
        ## iteration method
        '''
        parnetX = None
        parnetY = None
        depthX = 1
        depthY = 1
        depth = 1
        level = [root]
        while level:
            queue = []
           
            for node in level:
                if node.left:   
                    if node.left.val == x:
                        depthX = depth + 1
                        parnetX = node
                    if node.left.val == y:
                        depthY = depth + 1
                        parnetY = node 
                    queue.append(node.left)
                if node.right:
                    if node.right.val == x:
                        depthX = depth + 1
                        parnetX = node         
                    if node.right.val == y:
                        depthY = depth + 1
                        parnetY = node
                    queue.append(node.right)
            level = queue
            depth = depth + 1
        print("parnetX = {} parnetY = {} depthX = {} depthY = {}".format(parnetX.val,parnetY.val,depthX,depthY))
        if depthX == depthY and parnetX != parnetY:
            return True
        else:
            return False
        '''


        ## recursion method
        ## Runtime: 20 ms, faster than 99.82% of Python3 online submissions for Cousins in Binary Tree.
        ## Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Cousins in Binary Tree.
        self.ans = []
        def dfs(node,x,level,parnet):
            if node.val == x:
                self.ans.append(level)
                self.ans.append(parnet)
            else:
                if node.right:
                    dfs(node.right,x,level+1,node)
                if node.left:
                    dfs(node.left,x,level+1,node)
        dfs(root,x,0,root)
        dfs(root,y,0,root)
        print("[0]={} [1]={} [2]={} [3]={}".format(self.ans[0],self.ans[1].val,self.ans[2],self.ans[3].val))
        return (self.ans[0] == self.ans[2]) and (self.ans[1] != self.ans[3])
            
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

    ## level 2
    root.left = node2
    root.right = node3

    ## level 3
    
    #node2.left = node4
    node2.right = node5
    node3.left = node6 
    node3.right = node7
    
    a = Solution()
    #a.printLVR(root)
    ans = a.isCousins(root,3,7)
    #ans = a.getDepth(root,node6)
    print("ans = {}".format(ans))
    
    




if __name__ == '__main__':
    main()
        