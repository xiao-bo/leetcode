# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ## first method
        ## Runtime: 56 ms, faster than 98.70% of Python online submissions for Palindrome Linked List.
        ## Memory Usage: 32.3 MB, less than 6.90% of Python online submissions for Palindrome Linked List.
        ## time complexity is O(n)
        ## space complexity is O(n)
        '''
        num = []
        while head:
            num.append(head.val)
            head = head.next
        print(num)
        flag = True
        length = len(num)
        for x in range(0,length):
            print("nums[{}] = {}  nums[{}] = {}".format(x,num[x],length-x-1,num[length-x-1]))
            if num[x] == num[length-x-1]:
                continue
            else:
                flag = False
                break

        
        return flag
        '''
        ## second method
        ## Runtime: 76 ms, faster than 34.63% of Python online submissions for Palindrome Linked List.
        ## Memory Usage: 30.9 MB, less than 34.48% of Python online submissions for Palindrome Linked List.

        slow = fast = head
        ## get midpoint
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(" slow = {}".format(slow.val))
        slow = self.reverse(slow)
        self.printAllnode(slow)
        while head and slow:
            if head.val != slow.val:
                return False
            else:
                head = head.next 
                slow = slow.next
        return True
        
    def reverse(self,head):
        prev = None
        next = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

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

    

    
    
    ans = a.isPalindrome(node1)
    #node1 = a.reverse(node1)
    print(ans)
    #a.printAllnode(node1)
    
    
    
    

    

if __name__ == '__main__':
    main()     