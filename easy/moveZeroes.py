class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ## bubble sort method
        ## Runtime: 2676 ms, faster than 5.01% of Python online submissions for Move Zeroes.
        ## Memory Usage: 13.1 MB, less than 5.06% of Python online submissions for Move Zeroes.
        '''
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                print("num[x] = {}, nums[y] = {}".format(nums[x],nums[y]))

                if nums[x] == 0:
                    nums[x],nums[y] = nums[y],nums[x]
                print(nums)

        print(nums)
        '''
        ## improved bubble method
        ## Runtime: 800 ms, faster than 5.01% of Python online submissions for Move Zeroes.
        ## Memory Usage: 13 MB, less than 5.06% of Python online submissions for Move Zeroes. 
        '''
        for x in range(0,len(nums)):
            if nums[x] == 0:
                for y in range(x+1,len(nums)):
                    if nums[y] != 0:
                        nums[x],nums[y] = nums[y], nums[x]
                        break
        print(nums)
        '''
        '''
        ## count zero's method
        ## Runtime: 40 ms, faster than 45.90% of Python online submissions for Move Zeroes.
        ## Memory Usage: 12.9 MB, less than 5.06% of Python online submissions for Move Zeroes.

        count = 0
        for x in nums:
            if x == 0:
                count += 1
        #print(count)
        y = 0
        for x in range(0,len(nums)):
            if nums[x]!= 0:
                nums[y] = nums[x]
                y = y + 1

        if count == 0:
            y = 0
        else:
            print(count)
            print(y)
            for x in range(y,y + count):
                nums[x] = 0
                print(x)
        print(nums)
        '''
        ## optimal solution
        ## Runtime: 36 ms, faster than 72.20% of Python online submissions for Move Zeroes.
        ## Memory Usage: 12.7 MB, less than 67.09% of Python online submissions for Move Zeroes.
        # zero = 0
        # for cur in range(0,len(nums)):
        #     if nums[cur] != 0:
        #         nums[cur],nums[zero] = nums[zero],nums[cur]
        #         zero = zero +1 
        # print(nums)

        # two pointer 
        # Runtime 196 ms Beats 30.7% Memory 15.5 MB Beats 96.7%
        zero = 0
        non_zero = 1
        while zero < len(nums) and non_zero < len(nums):
            if nums[zero] != 0:
                zero = zero + 1
                continue
            if nums[non_zero] == 0:
                non_zero = non_zero + 1
                continue
            if zero < non_zero:
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
            else:
                non_zero = non_zero + 1
            

def main():
    a = Solution()
    nums = [1,0,0]
    nums = [4,2,4,0,0,3,0,5,1,0]
    #nums = [0,1,0,3,12]
    a.moveZeroes(nums)


if __name__ == '__main__':
    main()