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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        

        queue = [(root.right,root.left)]
        while queue:
            node1, node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left,node2.right))
                queue.append((node1.right,node2.left))
        return True
        

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
    root.add('r',2)
    root.add('l',2)
    root.left.add('l',3)
    root.left.add('r',4)
    root.right.add('l',4)
    root.right.add('r',3)
    root.left.left.add('l',5)
    root.left.left.add('r',6)
    root.left.right.add('l',7)
    root.left.right.add('r',8)
    root.right.left.add('l',8)
    root.right.left.add('r',7)
    root.right.right.add('l',6)
    root.right.right.add('r',4)
    
    node = [root]
    print (node)
    for x in node:
        print(x)

    a = Solution()
    ans = a.isSymmetric(root)
    #ans = a.printNodeByLVR(root,"")
    #print(ans)

if __name__ == '__main__':
    main()