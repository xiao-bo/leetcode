class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## binary search method
        ## Runtime: 32 ms, faster than 6.92% of Python online submissions for First Bad Version.
        ## Memory Usage: 11.9 MB, less than 13.89% of Python online submissions for First Bad Version.
        
        right = n
        left = 1
        mid = left
        while left < right:
            mid = int((left + right) / 2)
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid+1
            
        return left
        
    def isBadVersion(self,version):
        if version <4:
            return False    
        else:
            return True

def main():
    a = Solution()
    n = 10
    a.firstBadVersion(n)


if __name__ == '__main__':
    main()

