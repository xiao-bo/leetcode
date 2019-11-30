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
        #Runtime: 40 ms, faster than 71.71% of Python online submissions for Linked List Cycle II.
        #Memory Usage: 18.7 MB, less than 18.87% of Python online submissions for Linked List Cycle II.


        past = set()
        curr = head 
        while curr!= None:
            if curr in past:
                return curr
            past.add(curr)
            curr = curr.next
            
        return None
    
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