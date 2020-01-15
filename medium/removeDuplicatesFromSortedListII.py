# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def deleteDuplicates(self, head: ListNode):
        ## Runtime: 32 ms, faster than 95.79% of Python3 online submissions for Remove Duplicates from Sorted List II.
        ## Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List II.
        tmp = current = ListNode(0)
        tmp.next = current.next = head
        if not head:
            return head

        while current and current.next and current.next.next:

            if current.next.val == current.next.next.val:
                delete = current.next
                ## find no duplicates
                while delete.next.val == delete.val:
                    delete = delete.next
                    if not delete.next:
                        break
                current.next = delete.next
                #print("current.next == current.next.next")
            else:
                #print("no")
                current = current.next

        return tmp.next

    def printall(self,node):
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
    node6 = ListNode(4)
    node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    #node6.next = node7 
    #a.printall(node1)
    tmp = a.deleteDuplicates(node1)
    a.printall(tmp)

if __name__ == '__main__':
    main()