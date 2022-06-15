from typing import List
'''

Question link:
https://leetcode.com/problems/running-sum-of-1d-array/submissions/
1480. Running Sum of 1d Array

'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # brute method because time complexity is O(n^2)
        # Runtime: 63 ms, faster than 37.53% of Python3 online submissions for Running Sum of 1d Array.
        # Memory Usage: 14.1 MB, less than 74.15% of Python3 online submissions for Running Sum of 1d Array.
        '''
        ret = []
        for index in range(0, len(nums)):
            ret.append(sum(nums[:index+1]))

        return ret
        '''

        # method 2 using dynamic programming
        # ret[index] = ret[index-1] + nums[index]
        # time complexity is O(n)
        # Runtime: 49 ms, faster than 66.72% of Python3 online submissions for Running Sum of 1d Array.
        # Memory Usage: 14.1 MB, less than 74.15% of Python3 online submissions for Running Sum of 1d Array.
        ret = []
        ret.append(nums[0])

        for index in range(1, len(nums)):
            ret.append(ret[index-1] + nums[index])

        return ret
