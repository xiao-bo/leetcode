class MinStack(object):

    #Runtime: 48 ms, faster than 94.84% of Python online submissions for Min Stack.
    #Memory Usage: 15.7 MB, less than 62.22% of Python online submissions for Min Stack.
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []
        
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        self.stack.append(x)
        if not self.minstack :
            self.minstack.append(x)
        else:
            if self.minstack[-1] >= x:
                self.minstack.append(x) 

        #print(self.stack)
        #print(self.minstack)
        
    def pop(self):
        """
        :rtype: None
        """
        if self.minstack[-1] == self.stack[-1]:
            del self.minstack[-1]
        del self.stack[-1]
        
        #print(self.stack)
        #print(self.minstack)
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        else:
            #print(self.stack[-1])
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        else:
            return self.minstack[-1]
        
def main():
    a = MinStack()

    a.push(-2)
    a.push(0)
    a.push(-3)
    #a.push(0)
    print("get min = {}".format(a.getMin()))
    #print(a.top())
    a.pop()
    
    #print(a.getMin())
    a.top()
    print(a.getMin())
    #a.pop()
    #print(a.top())
    #print(a.getMin())


if __name__ == '__main__':
    main()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()