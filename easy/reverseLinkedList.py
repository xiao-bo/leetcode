# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):

    def reverseList(self, head):
        ##recursion method
        def recursionMethod(head, newhead):
            if head == None:
                return newhead
            
            next = head.next
            head.next = newhead

            return recursionMethod(next, head)

        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ans = recursionMethod(head,None)
        return ans
        ##recursion

        #iteration
        #Runtime: 28 ms, faster than 28.69% of Python online submissions for Reverse Linked List.
        #Memory Usage: 13.5 MB, less than 84.26% of Python online submissions for Reverse Linked List.
        
        '''
        prev = head
        if prev == None:
            return None

        curr = head.next
        if curr == None:
            return prev

        third = head.next.next
        
        
        while third:
            curr.next = prev
            prev = curr
            curr = third
            third = curr.next

        if third == None:
            curr.next = prev
            head.next = None
        return curr
        '''


    def printAllnode(self,node):
        x = 0
        while node:
            print(node.val)
            node = node.next
            x = x + 1
            if x > 5:
                break
    
def main():
    a = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    #node4 = ListNode(4)
    #node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    #node3.next = node4
    #node4.next = node5


    ans = a.reverseList(node1)
    #print(ans)
    a.printAllnode(ans)
    
    
    

    

if __name__ == '__main__':
    main()     