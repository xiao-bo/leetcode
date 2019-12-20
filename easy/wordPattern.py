class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
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
        #       print(dic[x])
        
def main():
    a = Solution()
    pattern = 'ba'
    #string = "dog cat cat dog"
    string = "dog ca"
    print(a.wordPattern(pattern, string))

if __name__ == '__main__':
    main()