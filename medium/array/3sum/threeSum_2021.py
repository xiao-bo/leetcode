from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []

        result = []

        # brute method time complexity O(n^3)
        # Time Limit Exceeded
        '''
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
        '''
        # method 2: reduce brute by a+b = -c, time complexity = O(n^2)
        nums.sort()

        for x in range(0, length):
            for y in range(x+1, length):
                if -(nums[x] + nums[y]) in nums[y+1:]:
                    print(f'y = {y}, nums[y:] = {nums[y:]}')
                    print(nums[x],nums[y],nums[x]+nums[y])
                    element = [nums[x], nums[y], -(nums[x]+nums[y])]
                    result.append(tuple(element))

        result = list(set(result))
        print(result)
        
        # remove depulicated element
        for x in range(0,len(result)):
            result[x] = list(result[x])
        
        return result