from time_needed_to_buy_tickets import Solution

def test_solution():

    s = Solution()
    
    assert s.timeRequiredToBuy([2,3,2], 0) == 4
    assert s.timeRequiredToBuy([2,3,2], 1) == 7
    assert s.timeRequiredToBuy([2,3,2], 2) == 6

    
    
    assert s.timeRequiredToBuy([5,1,1,1], 0) == 8
    assert s.timeRequiredToBuy([5,1,1,1], 1) == 2
    

    
    assert s.timeRequiredToBuy([5,1,2,3,4], 0) == 15
    assert s.timeRequiredToBuy([5,1,2,3,4], 1) == 2
    assert s.timeRequiredToBuy([5,1,2,3,4], 2) == 7
    assert s.timeRequiredToBuy([5,1,2,3,4], 3) == 11
    assert s.timeRequiredToBuy([5,1,2,3,4], 4) == 14
    