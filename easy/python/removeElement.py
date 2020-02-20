class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(0,len(nums)):
            if nums[i] == val:
                nums[i] = None
                count = count +1
        print("init:"+str(nums))
        i = 0
        j = len(nums)-1
        tmp = 0
        flag = 0
        while i < len(nums) and i < j:
            if nums[i] != None:
                i = i+1
                continue
            if nums[j] == None:
                j = j-1
                continue

            #print("nums[{}] = {}  nums[{}] = {}".format(i,nums[i],j,nums[j]))
            
            
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            
            print(nums)
        return len(nums)-count

def main():
    a = Solution()
    array = [0,0,0,3,3,4,5,3,5,6,7]
    #array = [3,2,2,3]
    val = 3
    #array = [0,0]
    #array = [-1,0,0,0,0,3,3]
    a.removeElement(array,val)
    print(array)

if __name__ == '__main__':
    main()