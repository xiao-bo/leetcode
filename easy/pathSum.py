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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #a = [1,2,3]
        
        #print(sums(sum))
        result = False
        result2 = False
        
        print(sum)
        
        if sum == 0 :
            #
            return True
            
        elif sum < 0:
            return False
        elif sum > 0:
            if root is None:
                return False
            
            
            result = result or self.hasPathSum(root.left,sum-root.val)
            result2 = result2 or self.hasPathSum(root.right,sum-root.val)
            #result2 = False
            return result or result2
        
    

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
    
    root.add('r',1)
    root.left.add('l',1)
    root.left.add('r',4)
    #root.right.add('l',4)
    #root.right.add('r',5)
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
    #sum = [1,2,3]
    ans = a.hasPathSum(root,4)
    #print(a.hasPathSum(root,5))
    print(ans)
    #ans = a.printNodeByLVR(root,"")
    #print(ans)

if __name__ == '__main__':
    main()

