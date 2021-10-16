from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        # brute method 
        total_max = 0 
        for x in range(0, len(height)):
            for y in range(x+1, len(height)):
                current_max = min(height[x], height[y]) * (y - x)
                total_max = max(current_max, total_max)

        return total_max
        '''
        # method2,  head and tail pointer
        # Runtime: 1218 ms, faster than 9.44% of Python3 online submissions for Container With Most Water.
        # Memory Usage: 27.7 MB, less than 22.84% of Python3 online submissions for Container With Most Water.
        
        head = 0 
        tail = len(height) - 1 
        total_max_area = 0 
        count = 0
        while head < tail:
            current_max_area = self.find_current_area(height, head, tail)
            total_max_area = max(total_max_area, current_max_area)
            print(f'head = {head}, tail = {tail}, ')
            print(f'current_max_area = {current_max_area}')

            if height[tail] > height[head]:
                head = head + 1
            else:
                tail = tail -1 
            

        return total_max_area

    def find_current_area(self,height, head, tail):
        return (tail - head) * min(height[head], height[tail])

        