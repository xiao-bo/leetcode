class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## hash function
        ## Runtime: 36 ms, faster than 43.84% of Python online submissions for Isomorphic Strings.
        ## Memory Usage: 13.1 MB, less than 52.63% of Python online submissions for Isomorphic Strings.
        sDic = {}
        tDic = {}
        if len(s) != len(t):
            return False
        
        for x in range(0,len(s)):
            if sDic.get(s[x],-1) != tDic.get(t[x],-1):
                return False
            sDic[s[x]] = tDic[t[x]] = x
        return True

def main():
    a = Solution()
    s = "egc"
    t = "too"

    print(a.isIsomorphic(s,t))

if __name__ == '__main__':
    main()