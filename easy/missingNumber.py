class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ## Runtime: 136 ms, faster than 12.64% of Python online submissions for Missing Number.
        ## Memory Usage: 13.7 MB, less than 5.26% of Python online submissions for Missing Number.
        '''
        hashtable = {}
        for x in nums:
            hashtable[x] = 1
        for x in range(0,len(nums)):
            if x not in hashtable:
                return x
        return len(nums)
        '''

        # method 2
        # Runtime130 ms Beats 98.38% Memory15.1 MB Beats 81.38%
        compared = [x for x in range(0, len(nums)+1)]

        return sum(compared) - sum(nums)
