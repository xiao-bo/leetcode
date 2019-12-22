class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ## recursion method
        ## I insert () to every position in n-1 result 
        ## for example n = 2 , n = 1 is ()
        ## () have 3 position, 1(2)3 , so I insert () to 3 position
        ## then i use set to remove duplicate result.
        ## Runtime: 20 ms, faster than 80.00% of Python online submissions for Generate Parentheses.
        ## Memory Usage: 12.3 MB, less than 5.88% of Python online submissions for Generate Parentheses.
        if n == 1:
            return ["()"]
        else: 
            tmp = set()
            s = self.generateParenthesis(n-1)
            #print("n = {} s = {}".format(n,s))
            for x in range(0,len(s)):
                for y in range(0,len(s[x])+1):
                    tmp.add(s[x][:y]+"()"+s[x][y:])
                    #print(s[x][:y]+"()"+s[x][y:])
            return list(tmp)
def main():
    a = Solution()
    
    n = 4
    ans = a.generateParenthesis(n)
    print(ans)

if __name__ == '__main__':
    main()
        

