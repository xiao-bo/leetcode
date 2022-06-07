from typing import List
class Solution:
    def validateStackSequences(
        self, pushed: List[int], popped: List[int]
    ) -> bool:
        # initialize stage
        # Runtime: 103 ms, faster than 44.45% of Python3 online submissions for Validate Stack Sequences.
        # Memory Usage: 14.2 MB, less than 7.18% of Python3 online submissions for Validate Stack Sequences.
        stack = []

        while pushed or popped:
            if len(pushed) == len(popped):
                stack.append(pushed.pop(0))
            print(pushed, stack, popped)
            if stack[-1] == popped[0]:
                print('pop')
                stack.pop()
                popped.pop(0)
            else:
                if pushed:

                    stack.append(pushed.pop(0))
                else:
                    break

        # 如果stack沒有值，代表True
        return len(stack) == 0

