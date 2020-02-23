class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        a = []
        for x in nums:
            if x not in a:
                a.append(x)
        print(a)
        for x in a:
            nums.remove(x)
        for x in nums:
            a.remove(x)
            
        return a[0]
        
        
def main():
    a = Solution()
    #nums = [2,2,1,3,3]
    nums = [1,2,2,3,3]
    #nums = [1]
    ans = a.singleNumber(nums)
    print(ans)

if __name__ == '__main__':
    main()