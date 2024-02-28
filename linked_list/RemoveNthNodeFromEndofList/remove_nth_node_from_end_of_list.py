class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use stack to record nth node
        # Runtime 44ms Beats 17.28% of users with Python3
        # Memory 16.56MB Beats 65.43% of users with Python3
        stack = []
        cur = head
        tmp = None
        if not head.next:
            return None
        while cur:
            stack.append(cur)
            cur = cur.next

        count = n
        while count > 0:
            tmp = stack.pop()
            count = count -1

        if len(stack) >= 1:
            pre = stack.pop()
            pre.next = tmp.next
            return head
        else:
            return head.next

        
