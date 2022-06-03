from typing import List

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/


class Solution:

    
    def removeDuplicates(self, nums: List[int]) -> int:
        # method 1 using two index
        # Runtime: 134 ms, faster than 30.22% of Python3 online submissions for Remove Duplicates from Sorted Array.
        # Memory Usage: 15.8 MB, less than 7.08% of Python3 online submissions for Remove Duplicates from Sorted Array.
        
        i = 0
        remove_count = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    j = j + 1
                else:
                    break
        
            nums[i+1:] = nums[j:]
            
            print(nums)
            
            i = i + 1
        return (len(nums[:i]), nums[:i])

    
    

'''
s = Solution()
nums = [1, 1, 2]
res_k, res_nums = s.removeDuplicates(nums)
print(res_k, res_nums)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
res_k, res_nums = s.removeDuplicates(nums)
print(res_k, res_nums)
'''