class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for x in range(0,len(nums)):
            if nums[x] not in count:
                count[nums[x]] = 1
            else:
                count[nums[x]] = count[nums[x]]+1
        print(count)
        ansValue = float('-inf')
        ansKey = ""
        for x in count:
            print(x)
            if count[x] > ansValue:
                ansValue = count[x]
                ansKey = x
        print("key = {} value = {}".format(ansKey,ansValue))
        #print(ansValue)
        return ansKey

def main():
    a = Solution()
    array = [3,2,2,3,3,4,4,4,4,4,1,5,5]
    ans = a.majorityElement(array)
    #print(ans)


if __name__ == '__main__':
    main()