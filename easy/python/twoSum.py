
def twoSum(nums,target):
    
    length = len(nums)
    ans = 0
    #print 'len = '+str(length)
    for x in range(0,length):
        for y in range(x+1,length):
            
            ans = nums[x]+nums[y]
            
            if ans == target:
                print "nums[{}] = {} nums[{}] ={}  target={}".format(x,nums[x],y,nums[y],target)
                return [x,y]

nums = [2, 7, 11,15]
twoSum(nums,26)

