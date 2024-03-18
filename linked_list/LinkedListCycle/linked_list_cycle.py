# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 2019 solution
        # Runtime: 44 ms, faster than 32.86% of Python online submissions for Linked List Cycle.
        # Memory Usage: 18.7 MB, less than 13.48% of Python online submissions for Linked List Cycle.
        """
        past = set()
        while head!= None:
            if head in past:
                return True
            past.add(head)
            head = head.next
        """
        # 2022 solution
        # Runtime 58ms Beats 14.97% of users with Python3
        # Memory 17.27MB Beats 99.99% of users with Python3
        """
        if not head:
            return False
        cur = head
        while cur:
            if cur.val >= 200000:
                return True
            else:
                cur.val = 200000
                cur = cur.next

        return False
        """
        # 2024 solution by two pointer
        # Runtime 45ms Beats 64.77% of users with Python3
        # Memory 19.06MB Beats 83.93% of users with Python3
        slow = fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False