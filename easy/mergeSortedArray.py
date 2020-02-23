class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for x in range(0,n):
            for y in range(x,m+n):
                
                if nums2[x] == nums1[y]:
                    print("=== x = {} y = {}".format(x,y))
                    self.move(nums1,y,m+n)
                    nums1[y] = nums2[x]
                    
                    break
                elif nums2[x] != nums1[y] and nums2[x] < nums1[y] :
                    print("<<< x = {} y = {}".format(x,y))
                    self.move(nums1,y,m+n)
                    nums1[y] = nums2[x]
                    
                    break
                elif nums2[x] != nums1[y] and nums2[x] > nums1[y] :

                    
                    if nums1[y] == 0 and nums1[y-1] > nums1[y]:
                        nums1[y] = nums2[x]
                        break 
                    print(">>> x = {} y = {}".format(x,y))
                    #nums1[y] = nums2[x]
                    
                    
                    continue


    def move(self, nums1, index, m):
        pivot = 0
        ## find 0's location
        for x in range(0,m-1):
            if nums1[x] > nums1[x+1]:
                pivot = x+1
        for x in range(pivot,index,-1):
            nums1[x] = nums1[x-1] 
        print("=====")

def main():

    a = Solution()
    nums1 = [1,2,3,0,0]
    nums1 = [0]
    nums1 = [1,0]
    #nums1 = [-1,0,0,3,3,3,0,0,0]
    len1 = 1
    for x in range(0,len(nums1)-1):
        if nums1[x] <= nums1[x+1]:
            len1 = len1 + 1
        else:
            break
    print (len1)
    nums2 = [5,6]
    nums2 = [1]
    nums2 = [2]
    #nums2 = [1,2,2]
    len2 = len(nums2)
    a.merge(nums1,len1,nums2,len2)
    #a.move(nums1,0,len1)
    print(nums1)
if __name__ == '__main__':
    main()