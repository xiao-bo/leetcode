class MinStack_2023:
    # 2023 solution
    # Runtime63 ms Beats 70.1% Memory18.4 MB Beats 11.87%
    def __init__(self):
        self.minstack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if len(self.minstack) == 0:
            self.min = val
            # 把當前最小值存起來
            self.minstack.append((val, val))
        else:

            self.min = min(val, self.min)
            self.minstack.append((val, self.min))

    def pop(self) -> None:
        self.minstack.pop()
        if len(self.minstack) > 0:
            self.min = self.minstack[-1][1]
        else:
            self.min = float('inf')

    def top(self) -> int:
        return self.minstack[-1][0]

    def getMin(self) -> int:
        return self.minstack[-1][1]


class MinStack_2024:
    # using two stacks to store the min value
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)

    def pop(self) -> None:
        cur = self.stack.pop()
        if cur == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
