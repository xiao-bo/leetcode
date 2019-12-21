class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## method like 3sum problem
        ## Runtime: 92 ms, faster than 76.16% of Python online submissions for 3Sum Closest.
        ## Memory Usage: 12 MB, less than 6.45% of Python online submissions for 3Sum Closest.

        localmin = float('inf')
        globalmin = float('inf')
        local = 0
        globalTotal = 0
        nums[:] = sorted(nums)
        for x in range(0,len(nums)-2):
            left = x + 1
            right = len(nums)-1
            while left < right:
                print("x = {} left = {} right = {}".format(x,left,right))
                total = nums[x] + nums[left] + nums[right]
                diff = total - target 
                if diff < 0 :
                    left = left + 1
                elif diff > 0:
                    right = right - 1
                else:
                    return total
                if abs(diff) < localmin: 
                    localmin = abs(diff)
                    local = total
                    #print("local = {}".format(local))
            if localmin < globalmin:
                globalmin = localmin
                globalTotal = local
        print("globalMin = {} globalTotal = {}".format(globalmin,globalTotal))
        return globalTotal
def main():
    a = Solution()
    nums = [-1, 2, 1, -4]
    target = 3
    print(a.threeSumClosest(nums,target))

if __name__ == '__main__':
    main()