# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #Runtime: 52 ms, faster than 92.16% of Python online submissions for Remove Linked List Elements.
        #Memory Usage: 18.7 MB, less than 20.69% of Python online submissions for Remove Linked List Elements.

        ## if no node
        if head is None:
            return None

        ## if only 1 node
        if head.next is None:
            if head.val == val:
                return None
            else:
                return head

        cur = head.next
        prev = head

        ## remove head.val ==val
        while head.val == val and cur:
            head = cur
            prev = head
            cur = head.next
        
        if head.val == val:
            return None

        while cur :
            #print("cur = {} prev = {}".format(cur.val,prev.val))
            ## if tmp.val is equal val
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next

            cur = cur.next


        return head

    def printAllnode(self,node):
        while node:
            print(node.val)
            node = node.next

def main():
    a = Solution()
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(2)
    node5 = ListNode(3)
    node1.next = node2
    node2.next = node3
    #node3.next = node4
    #node4.next = node5

    

    
    
    ans = a.removeElements(node1,1)
    print("===")
    a.printAllnode(ans)
    
    
    
    

    

if __name__ == '__main__':
    main()     