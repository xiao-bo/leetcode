from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode):
        
        if not root:
            return True
        #print(tree)
        ## used inorder to check number sequence is small to large
        ## Runtime: 52 ms, faster than 14.29% of Python3 online submissions for Validate Binary Search Tree.
        ## Memory Usage: 15.4 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
        '''
        tree = self.LVR(root)
        for x in range(0,len(tree)-1):
            if tree[x] >= tree[x+1]:
                
                return False
        return True
        '''


        ## used definition to check root and child relationship.
        ## Runtime: 40 ms, faster than 84.78% of Python3 online submissions for Validate Binary Search Tree.
        ## Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
        return self.check(root,float('-inf'),float('inf'))

    def check(self,root:TreeNode,lowerBound:int,upperBound:int):
        print("root = {} lowerBound = {} upperBound = {}".format(root.val,lowerBound,upperBound))
        if root.val >= upperBound:

            return False
        if root.val <= lowerBound:
            return False
        if root.left:
            if root.left.val >= root.val:
                return False
            
            ans = self.check(root.left,lowerBound,root.val)
            if not ans:
                return False

        if root.right:
            if root.right.val <= root.val:
                return False
            
            ans = self.check(root.right,root.val,upperBound)
            if not ans:
                return False
        return True

    def LVR(self,root:TreeNode):
        res = []
        if not root:
            return None
        else:
            
            if root.left:
                res.extend(self.LVR(root.left))
            
            res.append(root.val)
            
            if root.right:
                res.extend(self.LVR(root.right))
            return res
    
def main():
    ## case 1
    
    root = TreeNode(-1)
    node1 = TreeNode(-2)
    node2 = TreeNode(0)
    root.left = node1
    root.right = node2

    ## case 2

    
    '''
    root = TreeNode(5)
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    node3 = TreeNode(3)
    node4 = TreeNode(6) 
    root.left = node1
    root.right = node2
    root.right.left = node3
    root.right.right = node4
    
    '''
    '''
    root = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(15)
    node3 = TreeNode(6)
    node4 = TreeNode(20) 
    root.left = node1
    root.right = node2
    root.right.left = node3
    root.right.right = node4
    '''
    a = Solution()
    print(a.isValidBST(root))
    #print(a.LVR(root)

if __name__ == '__main__':
        main()