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

        # brute method has very duplicated product step
        ans = []
        all_product = 1
        for i in range(0, len(nums)):
            all_product = all_product * nums[i]

        for i in range(0, len(nums)):
            ans[i] = all_product / nums[i]

        return ans[i]