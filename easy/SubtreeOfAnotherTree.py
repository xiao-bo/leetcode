class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # method1 iterative method
        # Runtime299 ms Beats 36.44% Memory14.6 MB Beats 94.79%
        if root is None and subRoot:
            # 其中一個有值時，代表錯誤
            return False
        elif root and subRoot is None:
            # 其中一個有值時，代表錯誤
            return False
        res = False
        queue = [root]
        while queue:
            current = queue.pop()
            if current is None:
                continue       
            if current.val == subRoot.val:
                res = self.isSame(current, subRoot)
            if res == True:
                return True
            else:
                queue.append(current.left)
                queue.append(current.right)
        return False
    
    def isSame(self, node, subRoot):
        if node is None and subRoot:
            # 其中一個有值時，代表錯誤
            return False
        elif node and subRoot is None:
            # 其中一個有值時，代表錯誤
            return False
        elif node is None and subRoot is None:
            # 其中一個有值時，代表錯誤
            return True
        if node.val == subRoot.val:
            return self.isSame(node.left, subRoot.left) and \
                   self.isSame(node.right, subRoot.right)

