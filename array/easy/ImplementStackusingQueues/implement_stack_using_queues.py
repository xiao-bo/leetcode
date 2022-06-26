class MyStack:
    # using brute method 
    # push is O(1), pop and top is O(n)

    # Runtime: 39 ms, faster than 65.76% of Python3 online submissions for Implement Stack using Queues.
    # Memory Usage: 13.9 MB, less than 72.44% of Python3 online submissions for Implement Stack using Queues.

    # using top_element to record top of stack
    # Runtime: 61 ms, faster than 9.81% of Python3 online submissions for Implement Stack using Queues.
    # Memory Usage: 14 MB, less than 23.27% of Python3 online submissions for Implement Stack using Queues.
    

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.top_element = 0
    def push(self, x: int) -> None:
        self.q1.append(x)

        self.top_element = x

    def pop(self) -> int:

        if len(self.q1) == 0:
            return None

        while len(self.q1) > 1:
            element = self.q1.pop(0)
            self.q2.append(element)
            self.top_element = element

        ret = self.q1.pop(0)

        while len(self.q2) != 0:
            # recorvery q1
            self.q1.append(self.q2.pop(0))

        return ret

    def top(self) -> int:
        return self.top_element
        

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()