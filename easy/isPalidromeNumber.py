class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        
        
        strx = str(x)
        ans = ''
        
        for i in range(0,len(strx)):
            if strx[i] == strx[len(strx)-i-1]:
                continue
            else:
                return False



        return True
        
        

def main():
    a = Solution()

    x = -12
    ans = a.isPalindrome(x)
    print(ans)

if __name__ == '__main__':
    main()