class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = nums[0]
        sumSub = nums[0]
        sumTmp = nums[0]
        diff = nums[0]
        for i in range(len(nums)):
             
            sumTmp = sumSub = nums[i]

            for j in range(i+1,len(nums)):
                sumTmp = sumTmp + nums[j]
                if sumTmp > sumSub:
                    sumSub = sumTmp
            print("i = {} sumSub= {}".format(i,sumSub))
                
            if sumSub > maxSub:
                maxSub = sumSub
        return maxSub

def main():
    a = Solution()
    array = [-2,1,-3,4,-1,2,1,-5,4]
    array = [3,-1,5]
    #array = [-1]
    ans = a.maxSubArray(array)
    print(ans)

if __name__ == '__main__':
    main()
