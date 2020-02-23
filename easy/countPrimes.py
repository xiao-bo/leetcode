class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        #Runtime: 3412 ms, faster than 7.09% of Python online submissions for Count Primes.
        #Memory Usage: 36.2 MB, less than 42.59% of Python online submissions for Count Primes.        import math
        
        import math

        primes = []
        if n == 1:
            return 0
        if n >2:
            primes.append(2)
        if n > 3:
            primes.append(3)
        flag = 0
        for x in range(5,n,2):
            comp = int(math.sqrt(x))
            for pri in primes:
                print("x = {} comp = {}".format(x,comp))
                if pri > comp:
                    break
                if x % pri != 0:
                    flag = 1
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                primes.append(x)
            print(primes)
        return len(primes)


def main():
    a = Solution()
    n = 15
    ans = a.countPrimes(n)
    print("ans = {}".format(ans))
    #y = [x for x in range(0,10)]
    #print(y)
    #print(y[4:10:2])

if __name__ == '__main__':
    main()