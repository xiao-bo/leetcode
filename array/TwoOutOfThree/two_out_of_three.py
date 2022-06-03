from typing import List
from collections import Counter 


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int],
        nums3: List[int]
    ) -> List[int]:
        # using set 
        # Runtime: 76 ms, faster than 87.71% of Python3 online submissions for Two Out of Three.
        # Memory Usage: 14.1 MB, less than 36.87% of Python3 online submissions for Two Out of Three.
        
        ret = {}
        ret = self.build_counter(set(nums1), ret)
        ret = self.build_counter(set(nums2), ret)
        ret = self.build_counter(set(nums3), ret)

        ret_list = []

        for key in ret:
            if ret[key] >= 2:
                ret_list.append(key)

        print(ret_list)
        

        return ret_list


        
    def build_counter(self, nums, ret):
        for n in nums:
            if n in ret:
                ret[n] = ret[n] + 1

            else:
                ret[n] = 1

        return ret