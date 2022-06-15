class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # using stack
        # Runtime: 49 ms, faster than 37.95% of Python3 online submissions for Backspace String Compare.
        # Memory Usage: 13.9 MB, less than 23.22% of Python3 online submissions for Backspace String Compare.
        s_ret = []

        s_ret = self.build_stack(s)
        t_ret = self.build_stack(t)

        return s_ret == t_ret

    def build_stack(self, data):
        ret = []
        for char in data:
            if char == '#':
                if ret:
                    ret.pop()
                else:
                    continue
            else:
                ret.append(char)
        return ret
