class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ## bubble sort
        ## Runtime: 20 ms, faster than 66.95% of Python online submissions for Sort Colors.
        ## Memory Usage: 11.8 MB, less than 51.28% of Python online submissions for Sort Colors.
        '''
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] > nums[y]:
                    nums[x],nums[y] = nums[y],nums[x]
        '''
        ## insertion sort
        ## Runtime: 28 ms, faster than 12.00% of Python online submissions for Sort Colors.
        ## Memory Usage: 11.8 MB, less than 56.41% of Python online submissions for Sort Colors.
        '''
        for x in range(1,len(nums)):
            tmp = nums[x]
            y = x -1
            while y >= 0 and tmp < nums[y]:
                nums[y+1] =nums[y]
                y = y -1
            nums[y+1]=tmp 
        '''
        ## selection sort
        ## Runtime: 24 ms, faster than 36.30% of Python online submissions for Sort Colors.
        ## Memory Usage: 11.7 MB, less than 76.92% of Python online submissions for Sort Colors.
        '''
        for x in range(0,len(nums)):
            minimun = float('inf')
            minIndex = -1
            for y in range(x,len(nums)):
                if nums[y] < minimun:
                    minimun = nums[y]
                    minIndex = y
            nums[x],nums[minIndex] = nums[minIndex],nums[x]
        '''
        

        print(nums)
def main():
    a = Solution()
    nums = [2,0,2,1,1,0,1,2,2,2,0,1,1,0]
    a.sortColors(nums)


if __name__ == '__main__':
    main()