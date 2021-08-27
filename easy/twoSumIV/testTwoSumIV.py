from twoSumIV import findTarget
from twoSumIV import bst_insert
from twoSumIV import TreeNode

def test_findTarget():
    
    nums = [5,3,6,2,4,None,7]
    k = 9
    bst = TreeNode(nums[0])
    for x in range(1, len(nums)):
        bst_insert(bst, TreeNode(nums[x]))

    assert findTarget(bst, 9) == True
    assert findTarget(bst,28) == False
    assert findTarget(bst,10) == True

    nums = [2,1,3]
    k = 4
    bst = TreeNode(nums[0])
    for x in range(1, len(nums)):
        bst_insert(bst, TreeNode(nums[x]))

    assert findTarget(bst, 4) == True

    assert findTarget(bst, 1) == False

    assert findTarget(bst, 3) == True
    
    nums = [1]
    k = 2
    bst = TreeNode(nums[0])
    for x in range(1, len(nums)):
        bst_insert(bst, TreeNode(nums[x]))

    assert findTarget(bst, k) == False
    