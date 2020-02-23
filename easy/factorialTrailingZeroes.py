class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #Runtime: 20 ms, faster than 46.99% of Python online submissions for Factorial Trailing Zeroes.
        #Memory Usage: 11.8 MB, less than 17.65% of Python online submissions for Factorial Trailing Zeroes.

        return 0 if n == 0 else int(n/5) + self.trailingZeroes(int(n/5))
        
def main():
    a = Solution()
    n = 125
    ans = a.trailingZeroes(n)
    print(ans)

if __name__ == '__main__':
    main()