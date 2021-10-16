from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []

        result = []

        # brute method time complexity O(n^3)
        # Time Limit Exceeded
        
        for x in range(0, length):
            for y in range(x+1, length):
                for z in range(y+1, length):
                    if nums[x] + nums[y] + nums[z] == 0:
                        element = sorted([nums[x], nums[y], nums[z]])
                        result.append(tuple(element))

        result = list(set(result))
        
        # remove depulicated element
        for x in range(0,len(result)):
            result[x] = list(result[x])

        return result
        
        # method 2: 
