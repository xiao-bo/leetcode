class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ## iteration method
        ## Runtime: 16 ms, faster than 86.66% of Python online submissions for Add Digits.
        ## Memory Usage: 11.8 MB, less than 33.33% of Python online submissions for Add Digits.
        while num > 9:
            digit = []
            tmp = num
            while tmp >= 1:
                digit.append(tmp%10)
                tmp = int(tmp / 10)
            num = sum(digit)
        return num


        
def main():
    a = Solution()
    num = 138
    print(a.addDigits(num))

if __name__ == '__main__':
    main()
