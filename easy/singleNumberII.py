class Solution(object):
    def singleNumberII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        print (int((sum(list(set(nums)))*3 - sum(nums))/2))
            
        return 0
        
        
def main():
    a = Solution()
    nums = [2,2,3,2]
    #nums = [0,1,0,1,0,1,99]
    #nums = [1]
    ans = a.singleNumberII(nums)
    print(ans)

if __name__ == '__main__':
    main()