from typing import List

# Problem link https://leetcode.com/problems/remove-element/solution/

class Solution:

    # method 1 using two index and be careful edge case
    # Runtime: 36 ms, faster than 53.11% of Python3 online submissions for Remove Element.
    # Memory Usage: 14.1 MB, less than 92.12% of Python3 online submissions for Remove Element.
    '''
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
    '''
    '''
    # method 2 offical solution
    # Runtime: 53 ms, faster than 11.60% of Python3 online submissions for Remove Element.
    # Memory Usage: 14.3 MB, less than 15.51% of Python3 online submissions for Remove Element.
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
            j = j + 1
        return (i, nums[:i])
    '''
    # method 3 improve method 1 by offical solution
    # Runtime: 41 ms, faster than 22.44% of Python3 online submissions for Remove Element.
    # Memory Usage: 14.2 MB, less than 47.72% of Python3 online submissions for Remove Element.
    def removeElement(self, nums: List[int], val: int) -> int:
        head = 0 
        tail = len(nums)  
        while head < tail:
            if nums[head] == val:
                nums[head] = nums[tail - 1]
                tail = tail - 1 
            else:
                head = head + 1

        return (tail, nums[:tail])
        