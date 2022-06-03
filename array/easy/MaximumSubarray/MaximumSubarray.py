from typing import List

class Solution:
    
    # method1 極慢，傷心，應該是sum太多次重複的欄位了
    # Runtime: 1624 ms, faster than 5.05% of Python3 online submissions for Maximum Subarray.
    # Memory Usage: 15 MB, less than 85.27% of Python3 online submissions for Maximum Subarray.
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        head = 0
        tail = 0
        while tail < len(nums):
            currentSum = sum(nums[head:tail+1])
            print(head, tail, currentSum, maxSum)
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum == 0 :
                head = tail

            if currentSum < nums[tail]:
                # currentSum = head + head+1 + ... tail
                # if currentSum < nums[tail] then currentSum is negative 
                # so head is change to tail
                head = tail
            else:
                tail = tail + 1

        return maxSum

    # Method 2 improve method 1 by reduce count of sum
    # Runtime: 60 ms, faster than 92.55% of Python3 online submissions for Maximum Subarray.
    # Memory Usage: 15 MB, less than 59.41% of Python3 online submissions for Maximum Subarray.
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = nums[0]
        head = 0
        tail = 0
        while tail < len(nums):
            currentSum = currentSum + nums [tail]
            #print(head, tail, currentSum, maxSum)
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum == 0 :
                head = tail

            if currentSum < nums[tail]:
                # currentSum = head + head+1 + ... tail
                # if currentSum < nums[tail] then currentSum is negative 
                # so head is change to tail
                head = tail
                currentSum = 0
            else:
                tail = tail + 1

        return maxSum