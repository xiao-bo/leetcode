# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        if head == None:
            return tmp
        while head.next != None:
            if head.next.val == head.val:
                head.next = head.next.next
                continue
            elif head.next.val != head.val:
                head = head.next

        return tmp

def main():
    a = Solution()

    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    tmp = a.deleteDuplicates(node1)
             
    tmp.printAllNode()

if __name__ == '__main__':
    main()


        