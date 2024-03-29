class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumArray =[]
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        sumArray = 0
        maxSum = float('-inf')
        
        for i in nums:
            
            if i > (sumArray+i):
                sumArray = i
                print("> {} ".format(sumArray))
            
            elif i <= sumArray+i:

                sumArray += i
                print(sumArray)
            if maxSum < sumArray:
                maxSum = sumArray
            
        
        
        #print(sumArray)
        return maxSum

def main():
    a = Solution()
    array = [-2,1,-3,4,-1,2,1,-5,4]
    #array = [-1,5,-1,10]
    array = [1,2]
    ans = a.maxSubArray(array)
    print(ans)

if __name__ == '__main__':
    main()
