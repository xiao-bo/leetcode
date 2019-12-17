class MyQueue(object):
    # Your MyQueue object will be instantiated and called as such:
    # obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.peek()
    # param_4 = obj.empty()

    ## Runtime: 12 ms, faster than 88.07% of Python online submissions for Implement Queue using Stacks.
    ## Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Implement Queue using Stacks.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self.stack1 :
                
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        #print(self.stack1)
        print("stack1 = {} stack2 = {}".format(self.stack1,self.stack2))
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        print("???")
        print("stack1 = {} stack2 = {}".format(self.stack1,self.stack2))
        print("finish push")
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        x = self.stack1.pop()
        self.stack1.append(x)
        return x

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

        return not(not self.stack1)
        
def main():
    a = MyQueue()
    a.push(5)
    a.push(6)
    a.push(7)
    print(a.pop())
    print(a.peek())
    print(a.empty())
    a.pop()
    print(a.empty())
    a.pop()
    print(a.empty())
if __name__ == '__main__':
    main()


