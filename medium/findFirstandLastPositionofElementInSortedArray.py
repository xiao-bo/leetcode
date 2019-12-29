class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        elif len(nums)== 1 and nums[0] == target:
            return [0,0]
        elif len(nums) == 1 and nums[0] != target:
            return [-1,-1]

        left = 0
        right = len(nums)-1
        
        
        ans = [-1,-1]

        while left < right:
            ## find mid and small part
            mid = (left + right) //2
            #print("left = {} right = {} mid = {}".format(left,right,mid))
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 

        if nums[left] == target:
            ans[0] = left
        else:
            return ans
            
        #print("ans = {}".format(ans))
        #print("left = {} right = {} mid = {}".format(left,right,mid))
        
        right = len(nums) - 1
        ## find bigger part
        while left < right:
            #print("left = {} right = {} mid = {}".format(left,right,mid))
            mid = (left + right)//2 + 1
            
           
            if nums[mid] <= target:
                left = mid 
            else:
                right = mid -1 
        if nums[right] == target:
            ans[1] = right
        
        #print("ans = {}".format(ans))


        return ans

def test():
    testNum    = [[1,2,3],[1,1], [],     [7],   [1],[1,7,7,7,8,8,8,9,10],[1,7,7,8,8,8,9,10],[4,4,4,4,4,4,4,4,4,4,5]] 
    testTarget = [   2   ,  1,    1  ,    7  ,   7,    7,                  7,4]
    ansNum =     [ [1,1] ,[0,1],[-1,-1],[0,0],[-1,-1],[1,3],[1,2],[0,9]]
    a = Solution()
    for x in range(0,len(testNum)):
        ans = a.searchRange(testNum[x],testTarget[x])
        if ans != ansNum[x]:
            print("false = {}".format(x))
            return False

    return True
def main():
    a = Solution()
    nums = [1,7,7,7,8,8,8]
    #nums = [5,6,7,8,9,10]
    target = 7
    #nums = [4,4,4,4,4,4,4,4,4,4,5]
    #target = 4
    #nums = [1,2,3]
    #target = 2
    nums = [1,1]
    target = 1
    ans = a.searchRange(nums,target)
    #print(test())
    print("ans = {}".format(ans))

if __name__ == '__main__':
    main()

