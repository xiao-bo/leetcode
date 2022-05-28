from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # brute method because time complexity is O(n^2)
        # Runtime: 63 ms, faster than 37.53% of Python3 online submissions for Running Sum of 1d Array.
        # Memory Usage: 14.1 MB, less than 74.15% of Python3 online submissions for Running Sum of 1d Array.
        ret = []
        for index in range(0, len(nums)):
            ret.append(sum(nums[:index+1]))

        return ret
