from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        
        #print(self.recursion(root,[]))




    def recursion(self,root:TreeNode,res:List[int]):
        ## Runtime: 32 ms, faster than 19.56% of Python3 online submissions for Binary Tree Inorder Traversal.
        ## Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.
    
        if root:
            res = self.recursion(root.left,res)
            res.append(root.val)
            res = self.recursion(root.right,res)
        return res


def main():
    root = TreeNode(1)
    #root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    #root = None
    a = Solution()
    ans = a.inorderTraversal(root)
    print(ans)


if __name__ =="__main__":
    main()
        
