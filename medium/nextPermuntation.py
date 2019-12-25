class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        ## it is very complex method by me.
        ## Runtime: 32 ms, faster than 40.39% of Python online submissions for Next Permutation.
        ## Memory Usage: 11.7 MB, less than 62.26% of Python online submissions for Next Permutation.
        i = len(nums)
        '''
        print("length = {}".format(i))
    
        most = self.checkDecending(nums)

        if most == len(nums)-1:
            print("it is descending order")
            nums[:] = sorted(nums)
        elif most == -1 * (len(nums)-1):
            print("it is ascending order")
            nums[-1],nums[-2] = nums[-2],nums[-1]
        else:
            if nums[-2] - nums[-1] < 0:
                ## x x x x small big
                nums[-1],nums[-2] = nums[-2],nums[-1]
            else:
                ## for 2,3,1 -> 3,2,1
                diff = [nums[x] - nums[x+1] for x in range(0,len(nums)-1)]
                changeIndex = 0
                print(diff)
                print(nums)
                for x in range(len(diff)-1,-1,-1):
                    #print("diff = {} x = {}".format(diff[x],x))
                    if diff[x] >= 0:
                        changeIndex = x-1
                    else:
                        break
                print("change index = {}".format(changeIndex))
                array = sorted(nums[changeIndex:])
                for x in range(0,len(array)):
                    if nums[changeIndex] == array[x] :
                        if array[x]!=array[x+1]:
                            currValue = array[x]
                            currIndex = x
                        else:
                            continue
                
                nextValue = array[currIndex+1]
                nextIndex = nums[changeIndex:].index(nextValue)
                print(nums[changeIndex], nums[nextIndex])
                print("array = {}".format(array))
                print("currValue = {} currIndex = {} nextValue = {} nextIndex = {}".format(currValue,currIndex,nextValue,nextIndex))
                nums[changeIndex], nums[nextIndex+changeIndex] = nums[nextIndex+changeIndex],nums[changeIndex]
                nums[changeIndex+1:] = sorted(nums[changeIndex+1:])
        print(nums)

        
        '''
        ## same concept as me, but it is from others code
        ## Runtime: 28 ms, faster than 70.33% of Python online submissions for Next Permutation.
        ## Memory Usage: 11.7 MB, less than 62.26% of Python online submissions for Next Permutation.
        i = len(nums) - 2 ## like changedIndex
        while i >= 0 and nums[i+1] <= nums[i]:
            i = i - 1
        
        if i >= 0:
            j = len(nums) - 1
            while j > 0 and nums[j] <= nums[i]:
                j = j -1
            nums[j],nums[i] = nums[i],nums[j]
            
        nums[i+1:]=sorted(nums[i+1:])
        print(nums)
    
    def checkDecending(self,nums):
        diff = [nums[x] - nums[x+1] for x in range(0,len(nums)-1)]
        most = 0
        for x in diff:
            if x >= 0:
                most = most + 1
            elif x < 0:
                most = most - 1
        
        return most
        


       
def main():
    a = Solution()
    #nums = [2,3,1] # -> 2,1,3
    #nums = [1,4,5,3,2]
    #nums = [1,4,4,5,2]
    #nums = [1,3,2]
    #nums = [4,5,3,2]
    #nums = [1,5,1,1,1]
    #nums = [5,4,7,5,3,2] #-> 5,5,2,3,4,7
    #nums = [1,4,5,5,4,3]
    nums = [3,2,1]
    #nums = [8,9,3,7,5,1]
    #nums = [5,4,1,3,2]
    #print(sorted(nums[1:]))
    #print(nums[:1]+sorted(nums[1:]))
    '''
    nums = [1,4,2,5,3]
    nums = [1,4,5,3,2]
    #nums = [1,5,4,2,4]
    
    
    nums = [3,2,1] # -> 1,2,3
    
    nums = [1,1,5] # -> 1,5,1
    nums = [1,5,1] # -> 5,1,1
    nums = [1,2,3,4] # -> 1,2,4,3
    nums = [1,4,3,2] # -> 2,1,3,4
    nums = [4,3,2,1] # -> 1,2,3,4
    nums = [2,4,3,1] # -> 3,1,2,4
    nums = [3,4,2,1] # -> 4,1,2,3
    #nums = [1,5,4,3,2] # -> 2,1,3,4,5
    #nums = [1,4,5,3,2] # -> 1,5,2,3,4
    '''
    a.nextPermutation(nums)

if __name__ == '__main__':
    main()
