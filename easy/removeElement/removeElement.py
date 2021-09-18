from typing import List

class Solution:

    # method 1 
    # Runtime: 36 ms, faster than 53.11% of Python3 online submissions for Remove Element.
    # Memory Usage: 14.1 MB, less than 92.12% of Python3 online submissions for Remove Element.
    def removeElement(self, nums: List[int], val: int) -> int:
        count_of_remove_element = 0 
        head = 0 # head index
        tail = len(nums) - 1  # tail index

        if head == tail:
            print(nums[head], val)
            if val != nums[head]:
                print('!=')
                return (1, nums)
            else:
                print('==')
                return (0,[])

        while head <= tail :
            #print(nums)
            if nums[head] == val and nums[tail] != val:
                nums[head],nums[tail] = nums[tail],nums[head] # swap
            if nums[head] != val:
                head = head + 1
            if nums[tail] == val:
                tail = tail - 1 
                count_of_remove_element = count_of_remove_element + 1
                
        print(f'count_of_remove_element = {count_of_remove_element} '
              f'nums[:{-count_of_remove_element}] = '
              f'{nums[:-count_of_remove_element]}')
        #print(nums[:-count_of_remove_element-1])
        return (len(nums) - count_of_remove_element, nums[:-count_of_remove_element])
