class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        hint1: sorted array
        hint2: modify nums1 in-place
        hint3: nums1 consists of m elements that are not 0 and n elements that are 0
        hint4: nums2 has n elements
        """
        # brute method
        # 1. swap zero element in num1 and element in num2
        # 2. num1 sort 
        # time complexity is O(nlogn)
        # 42ms Beats 66.98% of users with Python3
        # 17.44MB Beats 9.81% of users with Python3
        if n == 0:
            return 

        i = 0
        
        while i < n:
            # swap
            nums1[m], nums2[i] = nums2[i], nums1[m]
            i = i + 1
            m = m + 1
        nums1.sort()
