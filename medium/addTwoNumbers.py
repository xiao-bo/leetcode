class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class solution(object):
    def addTwoNumbers(self,l1,l2):
        #l1.val = 10
        #l1.next = l2
        #l1.next.data = 11
        ans = []
        div = 0
        rem = 0
        add = 0
        while l1 is not None and l2 is not None:
            add = l1.val+l2.val
            
            if add+div >= 10:
                rem = (add+div) % 10
                ans.append(rem)
                div = 1
                

            elif add+div < 10:
                ans.append(add+div)
                div = 0
           

            l1 = l1.next
            l2 = l2.next
        
        while l1 is None and l2 is not None :
        
            if div+l2.val>=10:
                rem = (div+l2.val)%10
                ans.append(rem)
                div = 1
            elif div+l2.val<10:
                ans.append(div+l2.val)
                div = 0

            l2 = l2.next
        
        while l1 is not None and l2 is None:
            
            if div+l1.val>=10:
                rem = (div+l1.val)%10
                ans.append(rem)
                div = 1
            elif div+l1.val<10:
                ans.append(div+l1.val)
                div = 0
                
                #ans.append(div)
            
            #div = 0
            l1 = l1.next
            
        if l1 is None and l2 is None and div==1:
            
            ans.append(div)
            div = 0 
        
        print ans

        #return l1.val+l2.val


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
z2 = ListNode(7)
z3 = ListNode(9)
z4 = ListNode(3)
z5 = ListNode(9)
z1.next = z2
z3.next = z4
z4.next = z5
'''
'''
a = solution()

a.addTwoNumbers(m1,n1)

a.addTwoNumbers(e1,d1)

a.addTwoNumbers(f1,g1)
a.addTwoNumbers(y1,t1)
a.addTwoNumbers(b4,b1)
a.addTwoNumbers(c1,c4)
a.addTwoNumbers(z1,z3)
