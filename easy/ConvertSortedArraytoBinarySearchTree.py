# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # method1  Runtime180 ms Beats 10.9% Memory15.5 MB Beats 83.75%
        node = TreeNode()
        length = len(nums)
        mid = int(length/2)
        if length == 0:
            return None 
        elif length == 1:
            node.val = nums[0]
            return node
        elif length >=2:
            node.val = nums[mid]
            node.right = self.sortedArrayToBST(nums[mid+1:])
            node.left = self.sortedArrayToBST(nums[:mid])
        
        return node
