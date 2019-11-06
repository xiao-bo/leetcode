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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        thisLevel = []
        
        if root:
            thisLevel.append(root)
        else:
            return []

        queueVal = []
        while thisLevel:
            nextLevel = []
            thisLevelVal = []
            for node in thisLevel:
                
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                thisLevelVal.append(node.val)
                
            thisLevel = nextLevel 
            queueVal.append(thisLevelVal)
        #print(queueVal)
             
        return queueVal[::-1]
        

    def printNodeByLVR(self,node,ans):
        
        if node.left != None:    
            ans = self.printNodeByLVR(node.left,ans)

        ans = ans + str(node.val)
        print (node.val)

        if node.right != None:
            ans = self.printNodeByLVR(node.right,ans)
        return ans
    
def main():
    root = TreeNode(1)
    
    root.add('l',2)
    
    root.add('r',3)
    root.left.add('l',4)
    #root.left.add('r',4)
    root.right.add('l',4)
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
    ans = a.levelOrderBottom(root)
    print(ans)
    #ans = a.printNodeByLVR(root,"")
    #print(ans)

if __name__ == '__main__':
    main()