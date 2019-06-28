class Solution(object):
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        if x > pow(2,31)-1:
            return 0
        if x < -pow(2,31):
            return 0
        if x == 0:
            return 0
        array = []
        while x %10 ==0:
            ## avoid 120 = 012
            x = int(x / 10)

        while x > 0:
            array.append(x % 10)
            x =int(x / 10)
        if x < 0:
            array.append('-')
        
        if x < 0:
            x = str(x)
            y = x[::-1]
            y = y[:len(y)-1]
            #print(y)
            array.append(y)
            #print(x)
        
        
        ans =''
        for x in array:
            ans += str(x)
        
        if int(ans) > pow(2,31)-1:
            return 0
        if int(ans) < -pow(2,31):
            return 0
        return ans

def main():
    a = Solution()
    target = 1534236469
    #print(target)
    #print(pow(2,31))
    ans = a.reverse(target)
    print(ans)

if __name__ == '__main__':
    main()