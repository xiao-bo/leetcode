class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## others solution
        ## Runtime: 580 ms, faster than 84.10% of Python online submissions for 3Sum.
        ## Memory Usage: 15.1 MB, less than 25.00% of Python online submissions for 3Sum.
        ans = []
        if not nums:
            return nums
        nums[:] = sorted(nums)

        
        i = 0
        print(nums)
        

        for i in range(0,len(nums)-2):

            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1  
            #print("i = {}, left = {}, right = {}".format(i,left,right))
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    print("i = {} left = {} right = {} nums[i] = {} nums[left] ={} nums[right]={}".format(i,left,right,nums[i],nums[left],nums[right]))
                    
                    while left < right and nums[left] == nums[left+1]:
                        left = left + 1 
                    while left < right and nums[right] == nums[right-1]:
                        right = right -1
                    left = left + 1
                    right = right - 1 
                elif total < 0:
                    left = left + 1
                else:
                    right = right -1              
        return ans
    

def main():
    a = Solution()
    nums = [-1, 0, 1, 2, -1, -4,2]
    #nums = [-2,0,0,2,2]
    #nums = [-4,2,2]
    #nums = [0,0,0,0]
    nums = [-2,1,4]
    #nums = [1,2,-2,-1]
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    ## output = [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]
    #nums = []
    ans = a.threeSum(nums)
    print(ans)

if __name__ == '__main__':
    main()