class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack method in 2023 year
        # Runtime122 ms Beats 36.96% Memory14.5 MB Beats 18.73%

        if len(tokens) == 0:
            return 0
        elif len(tokens) == 1:
            return int(tokens[0])

        s = []
        for char in tokens:
            if char in ["+", "-", "*", "/"]:
                # is operator

                post = int(s.pop(-1))
                pre = int(s.pop(-1))
                if char == "+":
                    tmp = pre + post
                if char == "-":
                    tmp = pre - post
                if char == "*":
                    tmp = pre * post
                if char == "/":
                    tmp = int(pre / post)
                s.append(tmp)
            else:
                # is digit
                s.append(char)

        return int(s.pop(-1))

    def evalRPN_2024(self, tokens: List[str]) -> int:
        # stack method in 2024 year
        # Runtime 61ms Beats 83.60% of users with Python3
        # Memory 17.16MB Beats 46.12% of users with Python3
        number_stack = []

        a = ['+', '-', '*', '/']
        for c in tokens:
            if c.lstrip('-+').isdigit():
                number_stack.append(int(c))
            elif c in a:
                cur = number_stack.pop()
                pre = number_stack.pop()
                tmp = self.__str_to_int(cur, pre, c)
                number_stack.append(tmp)

        return number_stack.pop()

    def __str_to_int(self, cur: int, pre: int, c: str) -> int:
        res = 0
        if c == "+":
            res = pre + cur
        elif c == "-":
            res = pre - cur
        elif c == "*":
            res = pre * cur
        elif c == "/":
            res = int(pre / cur)
        return res
