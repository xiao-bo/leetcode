class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Runtime 30ms Beats 88.52% of users with Python3
        # Memory 16.48MB Beats 91.33% of users with Python3
        if len(nums) == 0:
            return []
        
        left = right = nums[0]
        ret = []
        for i in range(0, len(nums)):
            if nums[i] + 1 in nums:
                # right 繼續往右
                right = nums[i] + 1
            else:
                if left == right:
                    ret.append(f"{left}")
                else:
                    ret.append(f"{left}->{right}")
                if i+1 < len(nums):
                    # 避免out of bound
                    left = right = nums[i+1]

        return ret
