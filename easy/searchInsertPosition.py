class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if i < len(nums):
                if target > nums[i] and target < nums[i+1]:
                    return i+1

def main():
    a = Solution()
    array = [1,3,5,6]
    #array = [-1,0,0,0,0,3,3]
    print(a.searchInsert(array,4))

if __name__ == '__main__':
    main()