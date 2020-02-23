# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        ## Runtime: 208 ms, faster than 22.73% of Python online submissions for Intersection of Two Linked Lists.
        ## Memory Usage: 41.8 MB, less than 30.67% of Python online submissions for Intersection of Two Linked Lists.
        
        if headA is None or headB is None:
            return None

        tmpA = headA
        tmpB = headB
        while headA is not headB :
            
            if headA is None:
                headA = tmpB
            else:
                headA = headA.next
            if headB is None:
                headB = tmpA    
            else:
                headB = headB.next

        return headA
        
    
def main():
    a = Solution()
    node1 = ListNode(4)
    node2 = ListNode(1)
    node3 = ListNode(8)
    node4 = ListNode(4)
    node5 = ListNode(5) 
    #node1.next = node2
    #node2.next = node3
    #node3.next = node4
    #node4.next = node5
    
    n1 = ListNode(4)
    n2 = ListNode(0)
    n3 = ListNode(1)
    n4 = ListNode(8)
    n5 = ListNode(4)
    n6 = ListNode(5)
    #n1.next = n2
    #n2.next = n3
    #n3.next = n4
    #n4.next = n5
    #n5.next = n6
    
    
    
    ans = a.getIntersectionNode(node1,n1)
    print(ans)
    #ans = ans.next
    #print(ans.val)

if __name__ == '__main__':
    main()     