from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # brute method 
        total_max = 0 
        for x in range(0, len(height)):
            for y in range(x+1, len(height)):
                current_max = min(height[x], height[y]) * (y - x)
                total_max = max(current_max, total_max)

        return total_max