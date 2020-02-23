class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## Runtime: 136 ms, faster than 12.64% of Python online submissions for Missing Number.
        ## Memory Usage: 13.7 MB, less than 5.26% of Python online submissions for Missing Number.
        hashtable = {}
        for x in nums:
            

            hashtable[x] = 1
        for x in range(0,len(nums)):
            if x not in hashtable:
                return x
        return len(nums)

def main():
    a = Solution()
    num = [3,0,1]
    print(a.missingNumber(num))

if __name__ == '__main__':
    main()