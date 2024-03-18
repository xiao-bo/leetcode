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
    def mergeTwoLists_2020(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 2020 solution
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

    def mergeTwoLists_2024(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
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

    head = a.mergeTwoLists_2020(node1, node4)
    head.printAllNode()

    while head is not None:
        # head.printAllNode()
        head = head.next

    # print(l2.val)


if __name__ == "__main__":
    main()