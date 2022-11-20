# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        while current:
            current = current.next
            count = count + 1
        
        if count % 2 == 0:
            target_count = int(count / 2)
        else:
            target_count = int(count/2)
            
        for i in range(0, target_count):
            head = head.next 

        return head
