from typing import List

class Solution:


    def removeElement(self, nums: List[int], val: int) -> int:
        swap_count = 0 # swap_count of duplicate element
        head = 0 # head index
        tail = len(nums) - 1  # tail index

        # if head == tail:
        #     if nums[head] != 
        #     return (1,nums)

        while head < tail :
            #print(nums)
            if nums[head] == val and nums[tail] != val:
                nums[head],nums[tail] = nums[tail],nums[head] # swap
                swap_count = swap_count + 1
            if nums[head] != val:
                head = head + 1
            if nums[tail] == val:
                tail = tail - 1 
                
        print(f'swap_count = {swap_count} nums[:{-swap_count-1}] = {nums[:-swap_count-1]}')
        #print(nums[:-swap_count-1])
        return (len(nums) - swap_count-1, nums[:-swap_count-1])
