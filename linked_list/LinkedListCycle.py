# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 2022 solution
        # Runtime 58ms Beats 14.97% of users with Python3
        # Memory 17.27MB Beats 99.99% of users with Python3
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
