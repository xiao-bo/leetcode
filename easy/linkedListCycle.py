# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ##Runtime: 1004 ms, faster than 5.02% of Python online submissions for Linked List Cycle.
        #Memory Usage: 18.1 MB, less than 80.14% of Python online submissions for Linked List Cycle.
        

        past = set()
        while head!= None:
            if head in past:
                return True
            past.add(head)
            head = head.next
            
        return False
    
def main():
    a = Solution()
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    node4.next = node2
    

    
    
    ans = a.hasCycle(node1)
    print(ans)
    
    
    
    

    

if __name__ == '__main__':
    main()     