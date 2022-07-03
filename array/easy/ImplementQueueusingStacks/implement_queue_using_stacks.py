class MyQueue:

    # using two stack to solve
    # Runtime: 46 ms, faster than 45.70% of Python3 online submissions for Implement Queue using Stacks.
    # Memory Usage: 14.1 MB, less than 22.30% of Python3 online submissions for Implement Queue using Stacks.
    def __init__(self):
        self.myqueue = []
        self.stack = []

    def push(self, x: int) -> None:
        while self.myqueue:
            self.stack.append(self.myqueue.pop())
        self.stack.append(x)

        while self.stack:
            self.myqueue.append(self.stack.pop())

    def pop(self) -> int:
        if self.myqueue:
            return self.myqueue.pop()

        else:
            return None

    def peek(self) -> int:
        if self.myqueue:
            ret = self.myqueue.pop()
            self.myqueue.append(ret)

            return ret

        else:
            return None
        

    def empty(self) -> bool:
        
        return len(self.myqueue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()