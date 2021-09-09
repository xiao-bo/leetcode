from typing import List

#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
class Solution:

    # method 1 using two index 
    # Runtime: 134 ms, faster than 30.22% of Python3 online submissions for Remove Duplicates from Sorted Array.
    # Memory Usage: 15.8 MB, less than 7.08% of Python3 online submissions for Remove Duplicates from Sorted Array.
    def removeDuplicates(self, nums: List[int]) -> int:
        #nums = [1,2]
        print(f'len = {len(nums)}')
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    j = j+1
                else:
                    break
                    
            nums[i+1:]=nums[j:]
            i = i + 1

        print(f'i = {i} nums[:{i}] = {nums[:i]}')
        #print(nums[:i])
        return (len(nums[:i]), nums[:i])
