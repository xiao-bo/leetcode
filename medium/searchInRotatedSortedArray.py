class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## it is solved by myself.
        ## first, I find the pivot by using two pointer.
        ## then depending target and nums[pivot] relationship,
        ## i will do binary search in left part or right part

        ## Runtime: 28 ms, faster than 65.58% of Python online submissions for Search in Rotated Sorted Array.
        ##Memory Usage: 12 MB, less than 51.02% of Python online submissions for Search in Rotated Sorted Array.
        if not nums :
            return -1
        if len(nums)==1:
            if target != nums[0]:
                return -1
            else:
                return 0
        
        fast = 0
        pivot = -1
        slow = 0
        ## find pivot by two pointer
        while slow < len(nums) and fast < len(nums):
            print(slow,fast)
            if nums[slow] > nums[fast]:
                break
            fast = fast + 2

        ## avoid fast too large
        if fast == len(nums):
            fast = fast - 1 
        if fast == len(nums)+1:
            fast = fast - 2

        print(fast)
        if nums[fast-1] > nums[fast]:
            pivot = fast 
        elif nums[fast-1] < nums[fast] and nums[fast-2] > nums[fast-1]:
            pivot = fast - 1 
        else:
            ## avoid 1,3,5 case, 
            pivot = 0 

        print("pivot = {}".format(pivot))
        
        if target > nums[-1]:
            ## target in left part
            left = 0
            right = pivot-1
        else:
            #target in right part
            left = pivot
            right = len(nums)-1
        flag = 0
        mid = -1

        while left <= right :
            ## do binary search
            mid = int((left+right) / 2)
            print(left,right)
            print(nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1


        return -1

        
def main():
    a = Solution()
    nums = [5,6,8,1,2,4]
    #nums = [1,3,5]
    target = 9

    ans = a.search(nums,target)
    print(ans)


if __name__ == '__main__':
    main()