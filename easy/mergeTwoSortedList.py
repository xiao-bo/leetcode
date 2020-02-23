# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None
    
    def printAllNode(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next
    
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        tmp = head 
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        while True:
            if l1 == None:
                tmp.next = l2
                break
            elif l2 == None:
                tmp.next = l1
                break

            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        return head.next
        
def main():
    a = Solution()
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(6)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(2)
    node5 = ListNode(4)
    node6 = ListNode(7)

    node4.next = node5
    node5.next = node6

    
    
    head = a.mergeTwoLists(node1,node4)
    head.printAllNode()
    
    while head is not None:
        #head.printAllNode()
        head = head.next

    #print(l2.val)

if __name__ == '__main__':
    main()