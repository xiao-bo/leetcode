class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        maxLen = max(len(a),len(b))
        ans = ""
        next = 0
        ## add 0 to head of string in order to
         
        if len(a) > len(b):
            for x in range(0,len(a)-len(b)):
                b = '0' + b
        elif len(a) < len(b):
            for x in range(0,len(b) - len(a)):
                a = '0' + a
        print(a)
        print(b)

        for x in range(maxLen-1,-1,-1):
            check = int(a[x]) + int(b[x]) + next 
            next = 0
            if check == 0 :
                ans = '0'+ ans
            elif check == 1:
                
                ans = '1' + ans
            elif check == 2:
                ans = '0' + ans
                next = 1
            elif check == 3:
                ans = '1' + ans
                next = 1

        if next == 1:
            ans = '1' + ans
        return ans

def main():
    a = Solution()
    str1 = '1'
    str2 = '10110'
    ans = a.addBinary(str1,str2)
    print(ans)

if __name__ == '__main__':
    main()