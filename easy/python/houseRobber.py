class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## recursion method
        ## time limit exceeded
        
        length = len(nums)

        if not nums:
            return 0
        '''
        if length == 1:
            return nums[0]
        else:
            return max(nums[0]+self.rob(nums[2:]),self.rob(nums[1:]))
        '''
        #Runtime: 28 ms, faster than 7.12% of Python online submissions for House Robber.
        #Memory Usage: 11.9 MB, less than 19.15% of Python online submissions for House Robber.
        #memo = [0,nums[0]]
        previous = 0
        current = 0
        
        #print(memo)
        for x in range(0,length):
            #memo.append(max(memo[x], memo[x-1]+nums[x]))
            tmp = current
            current = max(current, previous + nums[x])
            previous = tmp

        #print(memo[-1])
        return current
        
        
        #print("max0 = {}".format(max0))
        #print(tmp)
        
        
        #return max(max0,max1)

def main():

    a = Solution()
    #nums = [1,2,3,1]
    #nums = [2,7,9,3,1]
    #nums = [2,1,1,2]
    #nums = [1,2,1,1]
    #nums = [2,4,8,9,9,3]
    #nums = [1,3,1,3,100]
    #nums = [4,1,2,7,5,3,1]
    nums = [4,1,2,7,5,3,1]
    #nums = [2,7,4]
    #print(nums[2:])
    #nums = [x for x in range(1,5)]
    print(nums)
    ans = a.rob(nums)
    print(ans)

if __name__ == '__main__':
    main()