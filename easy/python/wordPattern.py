class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        '''
        ## mapping function
        ## Runtime: 16 ms, faster than 68.33% of Python online submissions for Word Pattern.
        ## Memory Usage: 11.9 MB, less than 14.29% of Python online submissions for Word Pattern.
        
        if len(pattern)<1 or len(str) <1:
            return False

        nums = str.split(" ")
        print(pattern)
        print(nums)
        
        if len(pattern) != len(nums):
            return False

        dic = {}
        y = 0
        dic2 = {}
        ## dic2 is in order to check pattern and str is 1 to 1 relation ship
        ## if it is not 1 to 1, then length of dic1 and dic2 is different.
        ## if it is 1 to 1, their length is same.
        ## for example of not 1 to 1. pattern = abbc str = dog cat cat dog
        for x in pattern:
            
            if x not in dic: 
                dic[x] = nums[y]
            y = y +1

        y = 0
        for x in nums:
            if x not in dic2:
                dic2[x] = pattern[y]
            y = y +1
        
        if len(dic)!=len(dic2):
            return False

        y = 0
        for x in pattern:
            if dic[x] != nums[y]:
                return False
                
            y = y+1
        return True
        '''
        ## another method by two dictionary 
        ## this method is better than mine
        ## Runtime: 16 ms, faster than 68.33% of Python online submissions for Word Pattern.
        ## Memory Usage: 11.9 MB, less than 14.29% of Python online submissions for Word Pattern.

        words = str.split(" ")
        if len(pattern) != len(words):
            return False
        pattern_map, word_map = {}, {}
        for i in range(0,len(pattern)):
            '''
            print(pattern_map)
            print(word_map)
            print(word_map.get(words[i],-1))
            print(pattern_map.get(pattern[i],-1))
            '''
            print("======")
            if pattern_map.get(pattern[i], -1) != word_map.get(words[i], -1):
                
                return False
            pattern_map[pattern[i]] = word_map[words[i]] = i
            
        return True
        #       print(dic[x])
        
def main():
    a = Solution()
    pattern = 'caac'
    string = "dog cat cat fish"
    #string = "dog ca"
    nums = string.split(" ")
    print(a.wordPattern(pattern, string))
    #print(map(pattern.find,pattern))
    #print(map(nums.index,nums))

if __name__ == '__main__':
    main()