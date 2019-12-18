class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashtable = {}
        #for x in nums:
        #    hashtable[x] = 1
        for x in range(0,len(nums)):
            if x not in nums:
                return x
        return len(nums)

def main():
    a = Solution()
    num = [3,0,1]
    print(a.missingNumber(num))

if __name__ == '__main__':
    main()