class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # brute method 
        # runtime 48ms Beats 54.80% of users with Python3
        # memory 17.32MB Beats71.09% of users with Python3
        
        # remove space
        s = s.replace(' ', '')
        # remove all non alpha
        s = ''.join([i for i in s if i.isalpha() or i.isnumeric()])
        
        # transfer s into lowercase
        s = s.lower()
        
        # check palindrome
        start = 0
        end = len(s)-1
        ret = True
        while start < end:
            if s[start] != s[end]:
                ret = False
                break
            start = start + 1
            end = end - 1
        return ret

        
