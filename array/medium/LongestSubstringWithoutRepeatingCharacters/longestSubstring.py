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

        #Runtime: 88 ms, faster than 26.35% of Python online submissions for Longest Substring Without Repeating Characters.
        #Memory Usage: 12.2 MB, less than 40.63% of Python online submissions for Longest Substring Without Repeating Characters.

        ## slide window
        '''
        if not s:
            return 0
        longest = s[0]
        left = 0
        flag = 0
        right = left
        current = ''
        index = 0
        while left < len(s) and right < len(s):
            
            
            print("left = {} right = {}".format(left,right))
            
            if s[right] not in current:
                current = current + s[right]
                right = right + 1
            else:
                
                c = s[right]
                index = current.find(c,left)
                current = current[index+1:]
                left = index + 1
            print('left = {} right = {} current = {}'.format(left,right, current))            
            if len(current) > len(longest):
                longest = current 
                

            
            if len(longest) + left > len(s):
                break
           
            
        return longest
        '''
        ## optimize slide windows
        ## Runtime: 64 ms, faster than 39.40% of Python online submissions for Longest Substring Without Repeating Characters.
        ## Memory Usage: 12.1 MB, less than 56.25% of Python online submissions for Longest Substring Without Repeating Characters.

        if not s:
            return 0
        longest = 0
        left = 0
        flag = 0
        right = 0
        current = set()
        index = 0
        while left < len(s) and right < len(s):
            
            
            print("left = {} right = {} s[right] = {}".format(left,right,s[right]))
            
            if s[right] not in current:
                current.add(s[right])
                right = right + 1
                longest = max(longest,right-left)
                
            else:
                
                current.remove(s[left])
                left = left + 1
            print('left = {} right = {} current = {}'.format(left,right, current))            
            
            
        return longest


        # 2022 solve it again
        # Runtime61 ms Beats 93.59% Memory14.1 MB Beats 51.2%
        # slide window
        if len(s) < 2:
            return len(s)
        hash_map = []
        max_len = 0
        for char in s:
            #print(f'char = {char} hash_map = {hash_map}')
            if char not in hash_map:
                hash_map.append(char)
            else:
                #print(hash_map)
                hash_len = len(hash_map)
                if max_len < hash_len:
                    max_len = hash_len
                index = hash_map.index(char)
                # 從重複的元素，加一後，繼續找最大值
                hash_map = hash_map[index+1:]
                hash_map.append(char)
                #print(f'位移後 {hash_map}')
        hash_len = len(hash_map)
        if max_len < hash_len:
            max_len = hash_len
        return max_len


        # 2024 solve it again by two pointer
        # Runtime 52ms Beats 77.13% of users with Python3 
        # Memory 16.72MB Beats 58.34% of users with Python3
        i = 0
        if len(s) <=1:
            return len(s)
        k = 1
        max_long = 1
        tmp = s[i]
        while k < len(s):
            if s[k] not in tmp:
                tmp = tmp + s[k]
                max_long = max(len(tmp), max_long)
                k = k + 1
            else:
                tmp = tmp[1:]
                i = i + 1
        return max_long
        
def main():
    a = Solution()
    #s = ''
    s = '12343456'
    #s = 'anviaj'
    #s = "abcabcbb"
    #s = 'bbbbb'
    #s = 'pwwkew'
    #s = 'bpfbhmipx'
    ans = a.lengthOfLongestSubstring(s)
    print(ans)


if __name__ == '__main__':
    main()
