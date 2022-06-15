class CustomStack:

    # Runtime: 176 ms, faster than 40.30% of Python3 online submissions for Design a Stack With Increment Operation.
    # Memory Usage: 14.9 MB, less than 36.18% of Python3 online submissions for Design a Stack With Increment Operation.
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.top = 0

    def push(self, x: int) -> None:
        # 放到stack的top


        if self.top == self.maxSize:
            # stack is full
            pass 
        else:
            self.stack.insert(self.top, x)
            self.top += 1

    def pop(self) -> int:
        if self.top == 0:
            # stack is empty
            return -1
        else:
            # list index 需要-1
            self.top -= 1
            return self.stack.pop(self.top)
            
    def increment(self, k: int, val: int) -> None:
        for i in range(0, min(k, self.top)):
            # 因為k可能比self.top大或小，
            # k or self.top選一個最小的，
            # 才能只改變stack的某些element
            self.stack[i] += val


