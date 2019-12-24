# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## iteration method by me
        ## I spend 30 min to solve it 
        ## Runtime: 20 ms, faster than 50.14% of Python online submissions for Swap Nodes in Pairs.
        ## Memory Usage: 11.8 MB, less than 22.73% of Python online submissions for Swap Nodes in Pairs.
        if not head or not head.next:
            return head
       
        prev = ListNode(0)

        ans = ListNode(0)
        ans = head.next

        while head and head.next:
            prev.next = head.next
            head.next = head.next.next
            prev.next.next = head
            head = head.next
            prev = prev.next.next
        
        
        return ans
        
    def printAllnode(self,head):
        while head:
            print(head.val)
            head = head.next

def main():
    a = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    #node1.next = node2
    #node2.next = node3
    #node3.next = node4
    #node4.next = node5
    #node5.next = node6

    

    ans = a.swapPairs(node1)
    
    
    a.printAllnode(ans)


if __name__ == '__main__':
    main()     