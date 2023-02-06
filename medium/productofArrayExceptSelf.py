class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute method, time complexity is (o^2)
        # Time limit exceeded
        ans = []
        for i in range(0, len(nums)):
            tmp = 1
            for j in range(0, len(nums)):
                if j == i:
                    continue
                tmp = tmp * nums[j]
            ans.append(tmp)
        return ans

        