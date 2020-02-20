# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        while 

    def printAllnode(self,head):
        while head:
            print(head.val)
            head = head.next

def main():
    a = Solution()
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(1)
    node4 = ListNode(3)
    node5 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    

    a.deleteNode(node1)
    
    
    a.printAllnode(node2)
    


if __name__ == '__main__':
    main()     