class Solution(object):
    ## 2022 solution  
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ## check length of s is even number
        if len(s) %2 !=0:
            return False
        ## split string into list
        strlist = [x for x in s]
        ans = []
        left = ['[','{','(']
        right = [']','}',')']
        print(strlist)
        for c in s:
            if c in left:
                ans.append(c)
            elif c in right:
                if not ans:
                    ## ans have c belonged right and ans is empty 
                    return False
                pop = ans.pop()
                tmp = self.change(c)
                
                if pop != tmp:
                    ## open brackets is not same as close brackets
                    return False
        print(ans)
        if ans:
            return False
        
        return True

    def change(self,c):
        if c == ']':
            return '[' 
        elif c =='}':
            return '{'                
        elif c ==')':
            return '('
            
    ## 2024 solution
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        left = ['(', '[', '{']
        right = [')', ']', '}']:
        stack = []

        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if len(stack) == 0:
                    return False

                tail = stack.pop()

                if mapping[c] == tail:
                    continue
                else:
                    return False
        return len(stack) == 0
           

def main():
    s = "()"
    a = Solution()
    ans = a.isValid(s)
    print(ans)


if __name__ == '__main__':
    main()
