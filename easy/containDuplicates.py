class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## brute method is time limit exceeded, time complexity is O(n^2)
        '''
        b = []
        if not nums:
            return False
        for x in nums:
            if x not in b:
                b.append(x)
            else:
                return True         
        else:
            return False 
        '''
        ## set concept
        #Runtime: 104 ms, faster than 76.75% of Python online submissions for Contains Duplicate.
        #Memory Usage: 17.2 MB, less than 59.26% of Python online submissions for Contains Duplicate.
        '''
        setNums = set(nums)

        if len(setNums) != len(nums):
            return True
        else:
            return False
        '''
        ## hash table
        #Runtime: 124 ms, faster than 8.94% of Python online submissions for Contains Duplicate.
        #Memory Usage: 17.7 MB, less than 14.81% of Python online submissions for Contains Duplicate.
        hashTable = {}
        for x in nums:
            try:
                hashTable.pop(x)
                return True
            except:
                hashTable[x] = 1
        
        return False
                
        

def main():
    a = Solution()
    nums =  [1,2,3,4]
    ans = a.containsDuplicate(nums)
    print(ans)
    #print(bool(5)^bool(4))
    #print(bool(3))


if __name__ == '__main__':
    main()