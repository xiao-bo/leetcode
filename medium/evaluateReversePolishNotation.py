class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack method
        # Runtime122 ms Beats 36.96% Memory14.5 MB Beats 18.73%

        if len(tokens) == 0:
            return 0
        elif len(tokens) == 1:
            return int(tokens[0])

        s = []
        for char in tokens:
            if char in ['+', '-', '*', '/']:
                # is operator

                post = int(s.pop(-1))
                pre = int(s.pop(-1))
                if char == '+':
                    tmp = pre + post
                if char == '-':
                    tmp = pre - post
                if char == '*':
                    tmp = pre * post
                if char == '/':
                    tmp = int(pre / post)
                s.append(tmp)
            else:
                # is digit
                s.append(char)

        return int(s.pop(-1))
