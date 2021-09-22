from bestTimetoBuyandSellStock import Solution

def testMaxProfit():
	s = Solution()
	prices = [7,1,5,3,6,4]
	result = s.maxProfit(prices)

	assert result == 5 

	prices = [7,6,4,3,1]
	result = s.maxProfit(prices)

	assert result == 0