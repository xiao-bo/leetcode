class Solution:
    def makeGood(self, s: str) -> str:

        # Runtime: 62 ms, faster than 27.02% of Python3 online submissions for Make The String Great.
        # Memory Usage: 13.9 MB, less than 60.48% of Python3 online submissions for Make The String Great.
        stack = []
        for current in s:
            if stack:
                # current 等於stack[-1]的大寫或小寫，但不等於stack[-1]
                if (current == stack[-1].upper() or current == stack[-1].lower()) \
                    and current != stack[-1]:
                    
                    # find adjacent index
                    element = stack.pop()
                    s = s.replace(f'{element}{current}', '')
                    continue

            stack.append(current)
        return s
        