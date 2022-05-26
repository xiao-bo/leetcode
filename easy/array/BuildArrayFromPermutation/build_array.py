from typing import List

class Solution():
    def buildArray(self, nums: List[int]) -> List[int]:
        
        # method 1 brute method 
        # Runtime: 267 ms, faster than 5.25% of Python3 online submissions for Build Array from Permutation.
        # Memory Usage: 14.2 MB, less than 7.31% of Python3 online submissions for Build Array from Permutation.
        ret = []
        for index in range(0 ,len(nums)):
            ret.append(nums[nums[index]])

        return ret

