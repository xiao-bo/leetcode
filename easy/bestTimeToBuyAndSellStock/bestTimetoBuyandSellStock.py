from typing import List
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:

    # method1 using two pointer
    # Runtime: 1144 ms, faster than 38.06% of Python3 online submissions for Best Time to Buy and Sell Stock.
    # Memory Usage: 25 MB, less than 95.38% of Python3 online submissions for Best Time to Buy and Sell Stock.
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0
        if not prices:
            return 0
        low = 0 
        high = 1
        max_profit = 0

        while high < len(prices):
            if prices[low] > prices[high]:
                low = high 
            else:
                current_max = prices[high] - prices[low] 
                max_profit = max(current_max, max_profit)

            high = high + 1

        return max_profit