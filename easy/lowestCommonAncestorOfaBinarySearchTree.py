# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ## Runtime: 88 ms, faster than 11.74% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
        ## Memory Usage: 20.1 MB, less than 6.82% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
        ## stupid method
        '''
        pRoute = self.getRoute(root,p)
        qRoute = self.getRoute(root,q)
        #print("p route = {} q route = {}".format(pRoute,qRoute))
        maxIndex = 0
        minLength = min(len(pRoute),len(qRoute))
        for x in range(0,minLength):
            if pRoute[x].val == qRoute[x].val:
                maxIndex = x
                continue
            else:
                break
        #print(maxIndex)
        targetNode = pRoute[maxIndex]
        #print(targetNode.val)
        return targetNode
        '''

        ## make sense method
        ## Runtime: 76 ms, faster than 32.22% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
        ## Memory Usage: 20.2 MB, less than 6.82% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.

        find = root
        while find:
            if find.val > q.val and find.val > p.val:
                find = find.left
            elif find.val < q.val and find.val < p.val:
                find = find.right
            else:
                return find
        

    def getRoute(self,root,target):
        route = []
        find = root
        while find.val != target.val:
            route.append(find)
            if find.val < target.val:
                find = find.right
            elif find.val > target.val:
                find = find.left
        route.append(find)
        
        return route

    def printLVR(self,root):

        if root == None:
            return None
        else:

            self.printLVR(root.left)
            print(root.val)
        self.printLVR(root.right)


def main():
    root = TreeNode(6)

    ## level2 
    node2 = TreeNode(2)
    node3 = TreeNode(8)

    ## level3 
    node4 = TreeNode(0)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(9)

    ## level4
    node8 = TreeNode(3)
    node9 = TreeNode(5)

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
    ans = a.lowestCommonAncestor(root,node6,node7)
    print("ans = {}".format(ans.val))
    
    




if __name__ == '__main__':
    main()
        