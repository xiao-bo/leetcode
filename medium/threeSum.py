class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:\
            # Runtime 2835 ms Beats 26.3% Memory 175 MB Beats 5.13%
        # two pointer
        if len(nums) == 3:
            if sum(nums) != 0:
                return []
            else:
                return [nums]
        nums.sort()
        # print(nums)
        result = []

        for first in range(0, len(nums)):
            second = first + 1
            third = len(nums)-1
            while second < third:
                total = nums[first] + nums[second] + nums[third]
                if total < 0:
                    second = second + 1
                elif total > 0:
                    third = third - 1
                else:
                    result.append((nums[first], nums[second], nums[third]))
                    second = second + 1
                    third = third - 1

        return list(set(result))
