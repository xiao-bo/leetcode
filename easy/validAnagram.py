class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## hash Table Method
        ## Runtime: 36 ms, faster than 84.65% of Python online submissions for Valid Anagram.
        ## Memory Usage: 12.5 MB, less than 100.00% of Python online submissions for Valid Anagram.

        
        sDic = {}
        tDic = {}
        for x in s:
            try:
                sDic[x] = sDic[x]+1
            except:
                sDic[x] = 1
        for x in t:
            try:
                tDic[x] = tDic[x]+1
            except:
                tDic[x] = 1
        #print(sDic)
        #print(tDic)

        return sDic == tDic
def main():
    a = Solution()
    
    s = "anagram"
    t = "nagaram"
    s = "aacc"
    #t = "ccac"
    print(a.isAnagram(s,t))

if __name__ == '__main__':
    main()