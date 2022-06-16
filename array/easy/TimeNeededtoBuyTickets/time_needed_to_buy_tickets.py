from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # brute method 
        # Runtime: 386 ms, faster than 5.80% of Python3 online submissions for Time Needed to Buy Tickets.
        # Memory Usage: 14.2 MB, less than 16.02% of Python3 online submissions for Time Needed to Buy Tickets.
        '''
        t = tickets.copy()
        q = queue.Queue()

        for x in tickets:
            q.put(x)
        second = 0
        index = 0
        len_queue = len(tickets)
        while tickets[k] != 0:
            if tickets[index] <=0:
                index = (index+1)%len_queue
                continue
            
            tickets[index] -= 1
            second +=1
            index = (index+1)%len_queue
            current = q.pop(0)
            q.append(current)

        return second
        '''
        ## improve brute method 
        # Runtime: 136 ms, faster than 5.80% of Python3 online submissions for Time Needed to Buy Tickets.
        # Memory Usage: 13.9 MB, less than 16.02% of Python3 online submissions for Time Needed to Buy Tickets.
        second = 0
        index = 0
        len_queue = len(tickets)
        q = tickets.copy()
        while tickets[k] != 0:
            if tickets[index] <=0:
                index = (index+1)%len_queue
                continue
            
            tickets[index] -= 1
            second +=1
            index = (index+1)%len_queue
            current = q.pop(0)
            q.append(current)

        return second