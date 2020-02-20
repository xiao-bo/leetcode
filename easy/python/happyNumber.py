class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        ##Runtime: 12 ms, faster than 97.99% of Python online submissions for Happy Number.
        #Memory Usage: 11.9 MB, less than 10.00% of Python online submissions for Happy Number.
        
        digital = self.intoDigital(n)
        y = 0
        while y < 10:
            sumDigital = 0
            for x in digital:
                sumDigital = sumDigital + x * x
            if sumDigital == 1:
                return True
            else:
                digital = self.intoDigital(sumDigital)
            y = y + 1
        return False


    def intoDigital(self,n):
        digital = []
        print("n = {}".format(n))
        while n >= 1:
            digital.append(int(n%10))
            n = n / 10
        print(digital)
        return digital

def main():
    a = Solution()
    n = 19
    ans = a.isHappy(n)
    
    print(ans)


if __name__ =='__main__':
    main()