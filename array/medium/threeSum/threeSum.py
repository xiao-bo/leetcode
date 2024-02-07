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

        # two pointer again
        # Runtime 1488 ms Beats 21.77% of users with Python3
        # Memory 177.35 MB Beats 5.09% of users with Python3
        nums.sort()
        result = []
        for t in range(0, len(nums)):
            i = 0
            j = len(nums) - 1
            while i != t and j != t and i < j:
                #print(i,j,t)
                tmp = nums[i] + nums[j]
                if tmp > -nums[t]:
                    j = j - 1
                elif tmp < -nums[t]:
                    i = i + 1
                elif tmp == -nums[t]:
                    result.append((
                        nums[i],
                        nums[j],
                        nums[t]
                    ))
                    i = i + 1
                    j = j - 1
        return list(set(result))
