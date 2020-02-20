class Solution:
    def isPowerOfTwo(self, n):
        

        #Runtime: 20 ms, faster than 57.15% of Python online submissions for Power of Two.
        #Memory Usage: 11.9 MB, less than 35.29% of Python online submissions for Power of Two.
        if n <= 0:
            return False
        elif n == 1:
            return True
        while n >= 2:
            if n % 2!= 0:
                return False
            n = n / 2 
            print('n = {}'.format(n))
        

        return True

def main():
    a = Solution()
    ans = a.isPowerOfTwo(-1)
    print(ans)

if __name__ == '__main__':
    main()