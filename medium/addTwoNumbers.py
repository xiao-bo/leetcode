class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class solution(object):

    def addTwoNumbers(self,l1,l2):
        # Runtime: 60 ms, faster than 66.42% of Python online submissions for Add Two Numbers.
        # Memory Usage: 11.9 MB, less than 27.21% of Python online submissions for Add Two Numbers.
        ans = []
        flag = 0
        
        cur = head = ListNode(0)
        
        
        if not l2:
            return l1
        if not l1:
            return l2

        while l1 or l2:
            
            nextVal = 0
            if l1:
                nextVal = nextVal + l1.val
                l1 = l1.next 
            if l2:
                nextVal = nextVal + l2.val
                l2 = l2.next
            nextVal = nextVal + flag
            
            
            if nextVal >= 10:
                ten = nextVal /10
                unit = nextVal % 10
                ans.append(unit)

                head.next = ListNode(unit)

                flag = 1
            else:
                flag = 0
                ans.append(nextVal)
                head.next = ListNode(nextVal)
                
            head = head.next 
        if flag == 1:
            ans.append(flag)
            head.next = ListNode(flag)
            #head = head.next
        
        print(ans)
        return cur.next
        #


def main():
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    m1 = ListNode(5)
    m2 = ListNode(6)
    m3 = ListNode(4)
    #m4 = ListNode(8)
    m1.next = m2
    m2.next = m3
    #m3.next = m4

    e1 = ListNode(1)
    e2 = ListNode(8)
    e1.next = e2
    d1 = ListNode(0)

    f1 = ListNode(5)
    g1 = ListNode(5)

    t1 = ListNode(1)
    y1 = ListNode(9)
    y2 = ListNode(9)
    y1.next = y2

    b1 = ListNode(9)
    b2 = ListNode(1)
    b3 = ListNode(6)
    b4 = ListNode(0)
    b1.next = b2
    b2.next = b3

    c1 = ListNode(8)
    c2 = ListNode(9)
    c3 = ListNode(9)
    c4 = ListNode(2)
    c1.next = c2
    c2.next = c3

    z1 = ListNode(3)
    z2 = ListNode(5)
    z3 = ListNode(9)
    z4 = ListNode(3)
    z5 = ListNode(9)
    z1.next = z2
    z3.next = z4
    z4.next = z5
    '''
    '''
    a = solution()
    ## 243+564 = 708
    #a.addTwoNumbers(m1,n1)
    ## 18 + 0 = 18
    #a.addTwoNumbers(e1,d1)
    ## 5 + 5 = 01
    #a.addTwoNumbers(f1,g1)

    ## 1 + 99 = 0,0,1
    #a.addTwoNumbers(y1,t1)

    ##916 + 0 = 916
    #a.addTwoNumbers(b4,b1)
    ## 899 + 2 = 0,0,0,1
    #a.addTwoNumbers(c1,c4)
    ##37 + 939 = 2101
    ##36 + 939 = 2001
    ##35 + 939 = 299
    #a.addTwoNumbers(z1,z3)
    #print(a.addTwoNumbers(m1,n1))
    #print(a.addTwoNumbers(e1,d1))
    head = a.addTwoNumbers(f1,g1)
    
    #print(a.addTwoNumbers(y1,t1))
    #print(a.addTwoNumbers(b4,b1))
    #print(a.addTwoNumbers(c1,c4))
    #print(a.addTwoNumbers(z1,z3))
if __name__ == '__main__':
    main()