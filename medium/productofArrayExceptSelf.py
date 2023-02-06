class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute method has very duplicated product step
        # using math to solve it 
        # Runtime242 ms Beats 69.23% Memory21.4 MB Beats 47.61%
        ans = []
        if len(nums) <=2:
            return nums[::-1]
        if 0 in nums:
            ans = self.process_with_zero_element(nums)
        else:
            ans = self.process_without_zero_element(nums)

        return ans

    def process_with_zero_element(self, nums):
        all_product = 1
        zero_index = []
        ans = []
        
        for i in range(0, len(nums)):
            if 0 == nums[i]:
                zero_index.append(i)
            else:
                all_product = all_product * nums[i]

        if len(zero_index) >= 2 :
            # count of zero is equal or larger 2, 
            # then ans is full of zero
            ans = [0] * len(nums)
        else:
            # count of zero is 1 
            # then only zero index has product
            for i in range(0, len(nums)):
                if i in zero_index:
                    ans.append(all_product)
                else:
                    ans.append(0) 
        return ans
    def process_without_zero_element(self, nums):
        ans = []
        all_product = 1
        for i in range(0, len(nums)):
            all_product = all_product * nums[i]

        for i in range(0, len(nums)):
            ans.append(int(all_product / nums[i]))
        return ans

