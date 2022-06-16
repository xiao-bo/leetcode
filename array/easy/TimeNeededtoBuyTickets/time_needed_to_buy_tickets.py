from typing import List
import queue
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # brute method 
        # Runtime: 386 ms, faster than 5.80% of Python3 online submissions for Time Needed to Buy Tickets.
        # Memory Usage: 14.2 MB, less than 16.02% of Python3 online submissions for Time Needed to Buy Tickets.
        t = tickets.copy()
        q = queue.Queue()

        for x in t:
            q.put(x)
        second = 0
        index = 0
        len_queue = len(t)
        while t[k] != 0:
            print(t)
            if t[index] <=0:
                index = (index+1)%len_queue
                continue
            
            t[index] -= 1
            second +=1
            index = (index+1)%len_queue
            current = q.get()
            q.put(current)

        return second