# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def add(self,arrow,val):
        if arrow == 'l':
            self.left = TreeNode(val)
        elif arrow == 'r':
            self.right = TreeNode(val)
   
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1

    def printNodeByLVR(self,node,ans):
        
        if node.left != None:    
            ans = self.printNodeByLVR(node.left,ans)

        ans = ans + str(node.val)
        print (node.val)

        if node.right != None:
            ans = self.printNodeByLVR(node.right,ans)
        return ans
    
def main():
    root = TreeNode(3)
    
    root.add('l',2)
    
    root.add('r',4)
    root.left.add('l',1)
    #root.left.add('r',4)
    #root.right.add('l',4)
    root.right.add('r',5)
    '''
    root.left.left.add('l',5)
    root.left.left.add('r',6)
    root.left.right.add('l',7)
    root.left.right.add('r',8)
    root.right.left.add('l',8)
    root.right.left.add('r',7)
    root.right.right.add('l',6)
    root.right.right.add('r',4)
    root.right.right.add('r',4)
    root.right.right.right.add('r',4)
    '''
    #root.right.right.right.right.add('r',4)


    

    a = Solution()
    ans = a.isBalanced(root)
    print(ans)
    #ans = a.printNodeByLVR(root,"")
    #print(ans)

if __name__ == '__main__':
    main()