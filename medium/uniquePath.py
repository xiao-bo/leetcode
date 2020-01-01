class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        ## recursion method
        ## it can not pass the test case because of time limit exceeded.
        ## so recursion method have to be modified into dynamic method
        '''
        def recursion(m,n):
            #print("m = {} n = {} ".format(m,n))

            if m == 1 or n == 1:
                return m+n
            else:
                #print("???")
                return recursion(m-1,n)+recursion(m,n-1)
        if m -1 == 0 or n - 1 == 0:
            return 1
        return recursion(m-1,n-1)
        '''
        ## dynamic method
        ##Runtime: 16 ms, faster than 79.32% of Python online submissions for Unique Paths.
        ##Memory Usage: 11.8 MB, less than 34.48% of Python online submissions for Unique Paths.
        '''
        if m - 1 == 0 or n - 1 == 0:
            return 1

        nums = [[ 1 for x in range(0,m)]for y in range(0,n)]

        #print(nums)
        for x in range(1,n):
            for y in range(1,m):
                nums[x][y] = nums[x-1][y] + nums[x][y-1]
        
        #print(nums)
        return nums[n-1][m-1]
        '''
        ## math method 
        ## Runtime: 16 ms, faster than 79.32% of Python online submissions for Unique Paths.
        ## Memory Usage: 12 MB, less than 6.90% of Python online submissions for Unique Paths.
        n = n - 1 
        m = m - 1
        k = (n + m)
        ans = 1
        for x in range(0,k - max(n,m)):
            print("ans = {} k-x = {} min(n,m)-x = {}".format(ans,k-x,min(n,m)-x))
            ans = ans * (k-x)
            
            print(ans)
            
        for x in range(0,k-max(n,m)):
            ans = ans / (min(n,m)-x)
        print(ans)
        return int(ans)
        

def main():
    a = Solution()
    

    print(a.uniquePaths(4,6))

if __name__ == '__main__':
    main()