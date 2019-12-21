class Solution(object):
    def intersect(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        interestion = []
        for x in num1:
            if x in num2:
                interestion.append(x)
                num2.remove(x)
        print(interestion)

def main():
    a = Solution()
    nums2 = [1,2,2,1]
    nums1 = [2]
    a.intersect(nums1,nums2)

if __name__ == '__main__':
    main()