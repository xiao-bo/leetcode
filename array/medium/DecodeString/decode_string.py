class Solution:
    def decodeString(self, s: str) -> str:
        print('new start')
        n_stack = [] # number_stack
        c_stack = [] # c stack 
        tmp = ''
        num_tmp = ''
        decoded_string = ''
        decide = 0 #決定用+ or *
        flag = False
        for c in s:
            print(f'c = {c}, n_stack = {n_stack}, '
                  f'c_stack = {c_stack}, decoded_string = {decoded_string}'
                  f'decide = {decide}')
            if c.isdigit():
                num_tmp = num_tmp + c

            elif self.is_left_bracket(c):
                c_stack.append(c)
                n_stack.append(num_tmp)
                num_tmp = ''
                decide = decide + 1
            elif c.isalpha():
                if not n_stack:
                    # 如果n_stack is null，因為代表純英文而已
                    decoded_string = decoded_string + c
                    continue

                c_stack.append(c)
            elif self.is_right_bracket(c):
                print(n_stack)
                print(c_stack)
                if decide >= 2:
                    flag = True
                decide = decide - 1
                while c_stack[-1] != '[':
                    tmp = c_stack.pop() + tmp

                c_stack.pop()# pop [

                #if not c_stack : # stack is empty
                if not flag:
                    decoded_string = decoded_string +  int(n_stack.pop())* tmp
                #elif c_stack : # stack is not empty
                elif flag:
                    decoded_string =  int(n_stack.pop()) * (tmp + decoded_string)

                tmp = ''

        tmp = ''

        while not n_stack  and c_stack:
            tmp = c_stack.pop() + tmp

        decoded_string = decoded_string + tmp
        print(decoded_string)
        return decoded_string

    def is_left_bracket(self, c):
        return c == '['

    def is_right_bracket(self, c):
        return c == ']'
