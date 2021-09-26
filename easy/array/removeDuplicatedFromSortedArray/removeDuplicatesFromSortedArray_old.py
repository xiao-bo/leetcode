class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        pivot = 0
        i = 1
        if len(nums) < 1:
            ## if nums is empty
            return -1
        elif len(nums) == 1:
            return 1

        while pivot + i < len(nums):
            ## pivot compare to next element until encounter different element.

            if nums[pivot] == nums[pivot+i]:
                ## next element is same as pivot and next element becomes -1
                nums[pivot+i] = None
                i = i+1
            else:
                ## next element is not same as pivot,
                ## so pivot change to next element and initiate value of i
                pivot = pivot + i
                i = 1

        print (nums)
        i = j = 1

        while j < len(nums):
            ## move non-duplicated elements to overwrite location of duplicated element
            if nums[j] == None:
                j = j+1
            elif nums[i] == None:
                nums[i] = nums[j]
                nums[j] = None
                i = i+1
                j = j+1
            else:
                i = i+1
                j = j+1
        print (nums)
        length = 0
        i = 0
        while i < len(nums):
            if nums[i] != None :
                length = length + 1
            i = i+1


        print (nums)

        return length

def main():
    a = Solution()
    array = [0,0,0,3,3,4,5,5,6,7]
    array = [0,0]
    #array = [-1,0,0,0,0,3,3]
    print(a.removeDuplicates(array))

if __name__ == '__main__':
    main()