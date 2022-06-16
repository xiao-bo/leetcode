from time_needed_to_buy_tickets import Solution

def test_solution():

    s = Solution()
    tickets = [2,3,2]
    k = 2

    assert s.timeRequiredToBuy(tickets, 0) == 4
    assert s.timeRequiredToBuy(tickets, 1) == 7
    assert s.timeRequiredToBuy(tickets, 2) == 6

    
    tickets = [5,1,1,1]
    
    assert s.timeRequiredToBuy(tickets, 0) == 8
    assert s.timeRequiredToBuy(tickets, 1) == 2
    


    tickets = [5,1,2,3,4]
    
    assert s.timeRequiredToBuy(tickets, 0) == 15
    assert s.timeRequiredToBuy(tickets, 1) == 2
    assert s.timeRequiredToBuy(tickets, 2) == 7
    assert s.timeRequiredToBuy(tickets, 3) == 11
    assert s.timeRequiredToBuy(tickets, 4) == 14
    