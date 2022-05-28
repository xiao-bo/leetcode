from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        # brute method 
        # time complexity is O(n^2)
        # Runtime: 63 ms, faster than 66.31% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
        # Memory Usage: 14.1 MB, less than 25.37% of Python3 online submissions for Final Prices With a Special Discount in a Shop.
        ret = []
        for index in range(0, len(prices)):

            discount = self.__find_discount(prices, index)
            ret.append(prices[index] - discount)
        return ret

    def __find_discount(self, prices, index):

        target = prices[index]

        for x in range(index+1, len(prices)):

            if target < prices[x]:
                continue
            elif target >= prices[x]:
                return prices[x]

        return 0
