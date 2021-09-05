class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_insert(root, node):
    
    if root.val is None:
        root = node
    elif node.val is None:
    
        return True
    else:
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                bst_insert(root.left, node)
        elif root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                bst_insert(root.right, node)


def print_tree(root):
    if root != None:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)


# First Method
# Runtime: 227 ms, faster than 5.09% of Python3
# Memory Usage: 17.2 MB, less than 70.68% of Python3 
# online submissions for Two Sum IV - Input is a BST.

def traversalTree(root, target, hash_table):
    if root is None:
        return False
    print(f'root.val = {root.val}, target = {target}')

    if root.val in hash_table:
        return True
    else:
        hash_table.append(target - root.val)
        print(hash_table)
        return traversalTree(root.left, target, hash_table) or \
               traversalTree(root.right, target, hash_table)

    return False

# second method\
# using inorder sort
def traversalTree2(root, target):
    pass



def findTarget(root, target):
    #print_tree(root)

    hash_table = []
    #result = traversalTree(root, target, hash_table)
    result = False
    while root is not None
        result = traversalTree2(root.right, target - root.val) or \
                 traversalTree2(root.left, target - root.val)
        if result :
            break
        else:
            root = root.right 
    return result
    
    
nums = [5,3,6,2,4,None,7]
bst = TreeNode(nums[0])
for x in range(1, len(nums)):
    #print(f'current = {nums[x]}')
    bst_insert(bst, TreeNode(nums[x]))

result = findTarget(bst, 9)
print(result)
#nums = [2,1,3, None]
#print(findTarget(nums, 4))
