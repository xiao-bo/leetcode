class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n < 1:
            return error
        
        ans = [1,2]
        
        
        for x in range(0,n-2):
            ans.append(ans[x]+ans[x+1])
        
        return ans[n-1]
def main():
    a = Solution()
    print(a.climbStairs(10))

if __name__ == '__main__':
    main()