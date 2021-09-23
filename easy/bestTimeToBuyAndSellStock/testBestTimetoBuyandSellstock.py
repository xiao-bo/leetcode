from bestTimetoBuyandSellStock import Solution

def testMaxProfit():
    s = Solution()
    prices = [7,1,5,3,6,4]
    result = s.maxProfit(prices)

    assert result == 5 

    prices = [7,6,4,3,1]
    result = s.maxProfit(prices)

    assert result == 0

    prices = [7,8,100,1,2]
    result = s.maxProfit(prices)

    assert result == 93

    prices = [7,6,100,1,2]
    result = s.maxProfit(prices)

    assert result == 94


    prices = [7,8,100,1,101]
    result = s.maxProfit(prices)

    assert result == 100

    prices = []
    result = s.maxProfit(prices)

    assert result == 0

    prices = [1]
    result = s.maxProfit(prices)

    assert result == 0
