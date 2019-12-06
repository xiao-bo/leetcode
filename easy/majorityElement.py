class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## by dictionary 
        #Runtime: 148 ms, faster than 82.95% of Python online submissions for Majority Element.
        #Memory Usage: 13.3 MB, less than 75.61% of Python online submissions for Majority Element.
        
        count = {}
        
        
        for x in nums:
            if x not in count:
                count[x] = 1
            else:
                count[x] = count[x]+1
        
        print(count)

        
        ansValue = float('-inf')
        ansKey = ""
        for x in count:
            print(x)
            if count[x] > ansValue:
                ansValue = count[x]
                ansKey = x
        print("key = {} value = {}".format(ansKey,ansValue))
        return ansKey
        



def main():
    a = Solution()
    array = [3,2,2,3,3,4,4,4,4,4,1,5,5]
    ans = a.majorityElement(array)
    #print(ans)


if __name__ == '__main__':
    main()