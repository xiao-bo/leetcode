class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        ## Runtime: 200 ms, faster than 5.03% of Python online submissions for Bulls and Cows.
        ## Memory Usage: 11.9 MB, less than 37.50% of Python online submissions for Bulls and Cows.
        
        a = 0
        b = 0
    
        sNum = [int(x) for x in secret]
        yNum = [int(x) for x in guess]
        
        for x in range(0,len(sNum)):
            if sNum[x] == yNum[x]:
                a = a + 1
                sNum[x] = yNum[x] = -1
                
        for x in range(0,len(sNum)):
            if yNum[x] >= 0 and yNum[x] in sNum:
                b = b + 1
                i = sNum.index(yNum[x])
                sNum[i] = -2
                yNum[x] = -2
        print(a,b)
        #return str(a)+"A"+str(b)+"B"
        
        
        ## another method
        from collections import Counter
        s,g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        #print(s)
        #print(g)
        #print(s&g)
        #print((s&g).values())
        #print(sum((s&g).values()))
        print(a,sum((s&g).values())-a)
        #return '%sA%sB' % (a, sum((s & g).values()) - a)
        
        
        
        #return '%dA%dB' % (bulls, both - bulls)
def main():
    a = Solution()
    secret = '180777'
    guess = '781077'
    #secret = '123'
    #x = 2
    #secret = secret[:x]+secret[x+1:]
    #print(secret)
    #secret = '1123'
    #guess  = '0111'
    from collections import Counter
    print(Counter(secret))
    print(a.getHint(secret,guess))

if __name__ == '__main__':
    main()