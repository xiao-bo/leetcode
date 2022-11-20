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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 2022 solve it by recursion method 
        # Runtime64 ms Beats 23.37% Memory13.8 MB Beats 76%
        if p and q:
            if p.val == q.val:
                return (self.isSameTree(p.right, q.right)) and \
                    (self.isSameTree(p.left, q.left))
            else:
                return False
        elif p is None and q is None :
            return True
        else:
            return False

    '''
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #print("123")
        ans1 = ""
        ans2 = ""
        if p == None and q == None:
            return True
        elif q == None:
            return False
        elif p == None:
            return False


        ansLVR = self.printNodeByLVR(p,ans1)
        ansVLR = self.printNodeByVLR(p,ans1)

        ans2LVR = self.printNodeByLVR(q,ans2)
        ans2VLR = self.printNodeByVLR(q,ans2)

        if ans2LVR == ansLVR and ans2VLR == ansVLR:
            #print("is same")
            return True
        else:
            #print("is different")
            return False

    def printNodeByLVR(self,node,ans):
        
        if node.left != null:    
            ans = self.printNodeByLVR(node.left,ans)

        ans = ans + str(node.val)
        print (node.val)

        if node.right != None:
            ans = self.printNodeByLVR(node.right,ans)
        return ans
    def printNodeByVLR(self,node,ans):
        
        if node.left != None:    
            ans = self.printNodeByLVR(node.left,ans)

        ans = ans + str(node.val)
        print (node.val)

        if node.right != None:
            ans = self.printNodeByLVR(node.right,ans)
        return ans
    '''
def main():
    root = TreeNode(1)
    root.add('r','null')
    root.add('l',2)
    

    root2 = TreeNode(1)
    root2.add('l',2)
    #root3 = TreeNode([])

    a = Solution()
    ans = a.isSameTree(root,root2)
    print(ans)

if __name__ == '__main__':
    main()
