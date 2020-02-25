class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Runtime: 6188 ms, faster than 5.01% of Python online submissions for Longest Substring Without Repeating Characters.
        ## Memory Usage: 13.8 MB, less than 6.25% of Python online submissions for Longest Substring Without Repeating Characters.
        ## brute method
        '''
        if not s:
            return 0
        longest = s[0]
        
        for i in range(0,len(s)):
            current = ''
            for j in range(i,len(s)):
                if s[j] not in current:
                    current = current + s[j] 
                else:
                    break
            print('i = {} current = {}'.format(i, current))
            if len(current) > len(longest):
                longest = current 
            
        return len(longest)
        '''

        ## Runtime: 564 ms, faster than 11.20% of Python online submissions for Longest Substring Without Repeating Characters.
        ##Memory Usage: 12.1 MB, less than 59.38% of Python online submissions for Longest Substring Without Repeating Characters.

        if not s:
            return 0
        longest = s[0]
        i = 0
        flag = 0
        j = i
        current = ''
        index = 0
        while i < len(s):
            
            #current = ''
            #j = i
            print("i = {} j = {}".format(i,j))
            while j < len(s):
                if s[j] not in current:
                    current = current + s[j]
                else:
                    break
                print('i = {} j = {} current = {}'.format(i,j, current))            
                j = j + 1
                

            if len(current) > len(longest):
                longest = current 
            if j < len(s):
                c = s[j]
                index = current.find(c,i)
                current = current[index+1:]
                print('index = {} current = {}'.format(index,current))
                
                i = index + 1
            else:
                i = i + 1
            #    break
            #i = i+1
            if len(longest) + i > len(s):
                break
            flag = flag + 1
            if flag > 10:
                break
            
        return longest

def main():
    a = Solution()
    s = ''
    s = '1234345'
    #s = 'anviaj'
    #s = "abcabcbb"
    #s = 'bbbbb'
    #s = 'pwwkew'
    #s = 'bpfbhmipx'
    ans = a.lengthOfLongestSubstring(s)
    print(ans)


if __name__ == '__main__':
    main()
