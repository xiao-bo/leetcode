from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [1]


def main():
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    result = s.intersection(nums1, nums2)

    print(result)

if __name__ == '__main__':
    main()