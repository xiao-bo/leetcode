class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # tricky method
        # Runtime: 80 ms, faster than 10.08% of Python online submissions for Valid Perfect Square.
        # Memory Usage: 13.6 MB, less than 8.33% of Python online submissions for Valid Perfect Square.
        if num == 1 :
            return True
        if num == 2:
            return False
        for x in range(0,2**15):
            if x * x > num:
                return False
            elif x * x == num:
                return True
            
            print(x)
def main():
    a = Solution()
    num = 8
    
    print(a.isPerfectSquare(num))

if __name__ == '__main__':
    main()