from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # method 1 using built-in method
        # Runtime: 113 ms, faster than 49.73% of Python3 online submissions for Concatenation of Array.
        # Memory Usage: 14.3 MB, less than 24.37% of Python3 online submissions for Concatenation of Array.
        '''
        nums.extend(nums)

        return nums
        '''

        # method 2 using array
        # Runtime: 151 ms, faster than 17.29% of Python3 online submissions for Concatenation of Array.
        # Memory Usage: 14.3 MB, less than 24.37% of Python3 online submissions for Concatenation of Array.

        for index in range(0, len(nums)):
            nums.append(nums[index])

        return nums
