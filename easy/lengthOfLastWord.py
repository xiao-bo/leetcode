class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        array = s.split(" ")
        lenArray = len(array)
        #print (array)
        #print(array[lenArray-1] != '')
        for i in range(1,lenArray+1):
            #print(i)
            if array[lenArray-i] != '':
                #print('===b')
                return len(array[lenArray-i])

        
        return 0
        
        
def main():
    a = Solution()
    s = " b s "
    
    ans = a.lengthOfLastWord(s)
    print(ans)

if __name__ == '__main__':
    main()
