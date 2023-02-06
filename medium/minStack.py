class MinStack:
    # Runtime63 ms Beats 70.1% Memory18.4 MB Beats 11.87%
    def __init__(self):
        self.minstack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if len(self.minstack) == 0:
            self.min = val
            # 把當前最小值存起來
            self.minstack.append((val,val))
        else:
            
            self.min = min(val, self.min)
            self.minstack.append((val,self.min))
        
    def pop(self) -> None:
        self.minstack.pop()   
        if len(self.minstack)>0:
            self.min = self.minstack[-1][1]
        else:
            self.min = float('inf')
        
    def top(self) -> int:
        return self.minstack[-1][0]

    def getMin(self) -> int:
        return self.minstack[-1][1]

