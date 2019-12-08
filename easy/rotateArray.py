class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        ## it is brute method, time complexity is O(n*k) and can't pass test case
        '''
        while k > 0:
            tmp = nums[-1]
            for i in range(len(nums)-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = tmp
            k = k -1 
        '''
        ### it uses temporary list, in the end, replace 
        #Runtime: 56 ms, faster than 29.90% of Python online submissions for Rotate Array.
        #Memory Usage: 12.5 MB, less than 8.33% of Python online submissions for Rotate Array.
        ans = []
        for i in range(0,k):
            ans.append(nums[len(nums)-k+i])
        #print(ans)
        for i in range(0,len(nums)-k):
            ans.append(nums[i])
        #print(ans)
        for i in range(0,len(nums)):
            nums[i] = ans[i]
        print(nums)
def main():
    a = Solution()
    nums = [1,2,3,4,5,6,7]
    a.rotate(nums, 3)

if __name__ == '__main__':
    main()
        