from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]):
        '''
        x = 2
        if len(nums) < 3:
            return len(nums)
        prev = nums[0]
        current = nums[1]
        additionalNumber = 0
        
        ## it is solved by myself.
        ## Runtime: 64 ms, faster than 11.47% of Python3 online submissions for Remove Duplicates from Sorted Array II.
        ## Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array II.

        while x < len(nums):
            if prev == current and current == nums[x]:
                ## find third element is same as first and second
                nums[x-2] = 'F'
                additionalNumber = additionalNumber + 1
            prev = nums[x-1]
            current = nums[x]
            x = x + 1
        
        
        ## two pointer to move F to tail of list
        y = len(nums) - 1
        x = 0
        while x < y :
            if nums[x] == 'F':        
                ## find nums[y] is not F
                while nums[y] == 'F' and x < y:
                    y = y - 1
        
                nums[x],nums[y] = nums[y],nums[x]
                
                y = y - 1 
            
            x = x +1
        #print(nums) 
        #print(tmp)  
        if additionalNumber != 0:
            nums[:] = sorted(nums[:-additionalNumber])
            
        print(nums)        
        return len(nums) 
        '''
        from collections import Counter
        ## use counter and set to solve 
        ## Runtime: 56 ms, faster than 48.72% of Python3 online submissions for Remove Duplicates from Sorted Array II.
        ## Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array II.
        
        b = list(set(nums))
        diff = Counter(nums)
        number1 = []

        ## nums - set(nums) to find element whose number is 1.
        diff.subtract(Counter(b))
        #print(diff)
        for x in nums:
            ## find element whose number is 1
            if diff[x] == 0:
                number1.append(x)
        ans = []
        print(b)
        print(number1)
        for x in range(0,len(b)):
            
            if b[x] not in number1:
                ## insert element twice
                ans.append(b[x])
                ans.append(b[x])
            else:
                ## insert element once
                ans.append(b[x])
        nums[:] = sorted(ans[:])
        print(nums)
        return len(nums)
        

def main():
    a = Solution()
    nums = [1,1,1,2,2,3]
    nums = [0,0,1,1,1,1,2,3,3]
    nums = [-1,0,0,0,0,3,3]
    #nums = [1,2,2]
    #nums = [0,0,0,0,0]
    #nums = [0,1,2,2,2,2,2,3,4,4,4]
    #nums = [0,0,1,1,1,1,3,3,3,3,3]
    #nums = [1,1,1,1,1,1,1,2,2,2,3,3,4,5]
    #nums = [2,2,2,2,2,3,3,3,4,4,4,4]
    #nums = []
    print(a.removeDuplicates(nums))


if __name__ == '__main__':
    main()