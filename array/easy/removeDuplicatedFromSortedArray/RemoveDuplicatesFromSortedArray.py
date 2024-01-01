from typing import List

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/


class Solution:

    
    def removeDuplicates(self, nums: List[int]) -> int:
        # method 1 using two index
        # Runtime: 134 ms, faster than 30.22% of Python3 online submissions for Remove Duplicates from Sorted Array.
        # Memory Usage: 15.8 MB, less than 7.08% of Python3 online submissions for Remove Duplicates from Sorted Array.
        '''
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
        return len(nums[:i])
        ''' 
        # method2 
        # remove duplicate element + sorted
        # time complexity is O(nlogn)
        duplicated_nums = 0
        if len(nums) == 1:
            return len(nums) - duplicated_nums
        cur = nums[0]
        for x in range(1, len(nums)):
            if cur == nums[x]:
                nums[x] = float('inf')
                duplicated_nums = duplicated_nums + 1
            else:
                cur = nums[x]

        # inplace sorted
        nums.sort()
        return len(nums) - duplicated_nums
