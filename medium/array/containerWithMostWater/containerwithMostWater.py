from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        # brute method 
        max_water = 0 
        for x in range(0, len(height)):
            for y in range(x+1, len(height)):
                current_water = min(height[x], height[y]) * (y - x)
                max_water = max(current_water, max_water)

        return max_water
        '''
        # method2,  head and tail pointer
        # Runtime: 1218 ms, faster than 9.44% of Python3 online submissions for Container With Most max_water.
        # Memory Usage: 27.7 MB, less than 22.84% of Python3 online submissions for Container With Most max_water.

        head = 0 
        tail = len(height) - 1 
        max_water = 0 
        count = 0
        while head < tail:
            current_water = self.find_current_water(height, head, tail)
            max_water = max(max_water, current_water)
            print(f'head = {head}, tail = {tail}, ')
            print(f'current_water = {current_water}')

            if height[tail] > height[head]:
                head = head + 1
            else:
                tail = tail -1 
        

        return max_water

        '''
        method 3, improve brute method
        '''
        max_water = 0 
        for x in range(0, len(height)):
            for y in range(x+1, len(height)):
                current_water = min(height[x], height[y]) * (y - x)
                max_water = max(current_water, max_water)

        return max_water

    def find_current_water(self,height, head, tail):
        return (tail - head) * min(height[head], height[tail])

        