from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        # using stack
        # Runtime: 56 ms, faster than 68.34% of Python3 online submissions for Crawler Log Folder.
        # Memory Usage: 14.1 MB, less than 38.65% of Python3 online submissions for Crawler Log Folder.

        stack = []
        for log in logs:
            if log == '../' and stack:
                stack.pop()
            elif log == './':
                continue
            elif log == '../' and not stack:
                # on main folder
                continue
            else:
                stack.append(log)

        return len(stack)