class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #tmp = s[::-1]
        #s = tmp

        ## two index
        ## Runtime: 212 ms, faster than 88.12% of Python3 online submissions for Reverse String.
        ## Memory Usage: 17.3 MB, less than 98.84% of Python3 online submissions for Reverse String.
        j = len(s) - 1
        for i in range(0,int(len(s)/2)):
            s[i],s[j] = s[j],s[i]
            print(s)
            j = j - 1
        print("===")
        print(s)

        ## python method
        ## Runtime: 216 ms, faster than 80.42% of Python3 online submissions for Reverse String.
        ## Memory Usage: 17.5 MB, less than 91.86% of Python3 online submissions for Reverse String.
        s[:] = s[::-1]

def main():
    a = Solution()
    s =  ["h","e","l","l","o",'n']
    a.reverseString(s)

if __name__ == '__main__':
    main()
