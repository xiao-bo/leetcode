class Solution:
    def simplifyPath(self, path: str) -> str:
        # use stack to store the path
        # Runtime 39ms Beats 51.60% of users with Python3
        # Memory 16.55MB Beats 91.47% of users with Python3
        sp = path.split("/")
        stack = []
        for c in sp:
            if c == "..":
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            elif c == "" or c == "." or c == " ":
                continue
            else:
                stack.append(c)
        return "/" + "/".join(stack)
