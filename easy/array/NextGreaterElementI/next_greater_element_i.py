from typing import List


class Solution:
    def nextGreaterElement(
            self, nums1: List[int], nums2: List[int]) -> List[int]:

        # brute method time complexity n*m
        # Runtime: 404 ms, faster than 5.01% of Python3 online submissions for Next Greater Element I.
        # Memory Usage: 14.1 MB, less than 95.57% of Python3 online submissions for Next Greater Element I.
        ret = []
        for n1_index in range(0, len(nums1)):
            for n2_index in range(0, len(nums2)):
                
                next_greater = nums2[n2_index]
                if nums1[n1_index] != nums2[n2_index]:
                    continue

                elif nums1[n1_index] == nums2[n2_index]:
                    

                    # 假如找到一樣的值，就塞入nums2 index 後面最大的值
                    for k in range(1, len(nums2)-n2_index):
                        
                        if nums2[n2_index] < nums2[n2_index+k]:
                            next_greater = nums2[n2_index+k]
                            
                            ret.append(next_greater)
                            break
                if next_greater == nums2[n2_index]:
                    
                    ret.append(-1)
                break
       
       

        return ret