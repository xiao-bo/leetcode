class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        if len(s) == 1:
            return s
        current = ''
        longest = s[0]
        ## brute method
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                current = s[i:j+1]
                #print('i = {} j = {} current = {}'.format(i,j,current))
                if self.checkPalindrome(current):
                    if len(longest) < len(current):
                        longest = current 
        return longest

    def checkPalindrome(self,s):
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1 
        return True


def main():
    a = Solution()
    s = 'ac'
    #s = 'abbbd'
    ans = a.longestPalindrome(s)
    print("ans = {}".format(ans))

if __name__ == '__main__':
    main()