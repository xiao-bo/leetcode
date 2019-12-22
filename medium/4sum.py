class Solution(object):
    def threeSum(self, nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## based on three sum solution
        ## Runtime: 840 ms, faster than 29.72% of Python online submissions for 4Sum.
        ## Memory Usage: 11.7 MB, less than 95.45% of Python online submissions for 4Sum.
        
        ans = []

        if not nums:
            return nums
    
        for i in range(0,len(nums)-2):
            right = len(nums) - 1 
            left = i + 1
            if i == 0 or nums[i] != nums[i-1]: 
                
                #print("i = {}, left = {}, right = {}".format(i,left,right))
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total - target == 0:
                        ans.append([nums[i],nums[left],nums[right]])
                        #print("i = {} left = {} right = {} nums[i] = {} nums[left] ={} nums[right]={}".format(i,left,right,nums[i],nums[left],nums[right]))
                        
                        while left < right and nums[left] == nums[left+1]:
                            left = left + 1 
                        while left < right and nums[right] == nums[right-1]:
                            right = right -1
                        left = left + 1
                        right = right - 1 
                    elif total - target < 0:
                        left = left + 1
                    else:
                        right = right -1              
        return ans
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ans = [] 
        if not nums:
            return []
        nums[:]= sorted(nums)
        #print(nums)
        
        for x in range(0,len(nums)-3):

            if x == 0 or nums[x] != nums[x-1]:
                
    
                threeResult = self.threeSum(nums[x+1:],target-nums[x])

                for element in threeResult:
                    ans.append([nums[x]]+element)

                
        #print(ans)              
        return ans
def main():
    nums = [1, 0, -1, 0, -2, 2]
    nums = [-3,-2,-1,0,0,1,2,3]
    #nums = [0,0,0]
    target = 0
    
    
    #out          = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    #excepted out = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    nums = [-1,0,1,2,-1,-4] 
    target = -1
    #out = [[-4,0,1,2]]
    #exceptOut = [[-4,0,1,2],[-1,-1,0,1]]

    nums = [5,5,3,5,1,-5,1,-2]
    target = 4
    #out =  [[-5, 1, 3, 5], [-5, 1, 3, 5]]
    #exceptOut= [[-5,1,3,5]]
    
    a = Solution()
    ans = a.fourSum(nums,target)
    print(ans)

if __name__ == '__main__':
    main()