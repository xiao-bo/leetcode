class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ## Runtime: 16 ms, faster than 80.87% of Python online submissions for Ugly Number.
        ## Memory Usage: 11.8 MB, less than 38.46% of Python online submissions for Ugly Number.
        if num == 1:
            return True
        if num <= 0:
            return False
        while num > 1:
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                return False
            else:
                if num % 2 == 0:
                    num = num / 2
                if num % 3 == 0 :
                    num = num / 3
                if num % 5 == 0:
                    num = num / 5
        return True
        '''
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1
        '''
def main():
    a = Solution()
    i = -2147483648
    print(a.isUgly(i))

   
if __name__ == '__main__':
    main()