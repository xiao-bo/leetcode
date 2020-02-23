
def twoSum(nums,target):
    
    length = len(nums)
    ans = 0
    
    ## brute method
    ## Runtime: 4588 ms, faster than 21.40% of Python online submissions for Two Sum.
    ## Memory Usage: 12.5 MB, less than 84.59% of Python online submissions for Two Sum.
    '''
    for x in range(0,length):
        for y in range(x+1,length):
            
            if nums[x] + nums[y] == target:
                print "nums[{}] = {} nums[{}] ={}  target={}".format(x,nums[x],y,nums[y],target)
                return [x,y]
    '''
    ## hashTable
    ## Runtime: 32 ms, faster than 92.25% of Python online submissions for Two Sum.
    ## Memory Usage: 13.2 MB, less than 20.89% of Python online submissions for Two Sum.
    hashTable = {}
    for i in range(0,len(nums)):
        if target - nums[i] in hashTable:
            return [i,hashTable[target-nums[i]]]
        else:
            hashTable[nums[i]] = i
    
    
def main():
    nums = [2, 7, 11,15]
    print(twoSum(nums,26))
    

if __name__ == '__main__':
    main()

