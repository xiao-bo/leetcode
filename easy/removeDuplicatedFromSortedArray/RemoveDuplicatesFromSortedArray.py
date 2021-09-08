from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        #nums = [1,2]
        print(f'len = {len(nums)}')
        i = 0
        j = 1
        while i < len(nums):
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
