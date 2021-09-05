from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if (not nums1) or (not nums2):
            # check null 
            return False

        # method 1 using built-in function. 
        # Runtime: 48 ms, faster than 55.21% of Python3 online submissions for Intersection of Two Arrays.
        # Memory Usage: 14.5 MB, less than 46.88% of Python3 online submissions for Intersection of Two Arrays.
        #result = list(set(nums1).intersection(set(nums2)))


        # method 2 using hash table
        # Runtime: 64 ms, faster than 22.62% of Python3 online submissions for Intersection of Two Arrays.
        # Memory Usage: 14.2 MB, less than 91.32% of Python3 online submissions for Intersection of Two Arrays.
        result = set()
        for x in nums1:
            if x in nums2:
                result.add(x)
                nums2.remove(x)
        result = list(result)

        #         
        return result
        


def main():
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    result = s.intersection(nums1, nums2)

    print(result)

if __name__ == '__main__':
    main()