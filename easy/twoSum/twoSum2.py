def get_two_sum(nums, target):

    if len(nums) < 2:
        return []
    '''
    # brute method after work 1 years
    # Runtime: 4016 ms, faster than 24.64% of Python3 online submissions for Two Sum.
    # Memory Usage: 14.6 MB, less than 98.26% of Python3 online submissions for Two Sum.
    for x in range(0, len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]
    '''

    # list method by using hasing
    # Runtime: 640 ms, faster than 37.63% of Python3 online submissions for Two Sum.
    # Memory Usage: 14.7 MB, less than 98.26% of Python3 online submissions for Two Sum.
    '''
    for x in range(0, len(nums)):
        print(nums[x + 1:])
        if target - nums[x] in nums[x+1:]:
            y_index = find_index(nums, target - nums[x], x)
            return [x, y_index]
    '''
    
    # reduce list method time complexity 
    # Runtime: 640 ms, faster than 37.63% of Python3 online submissions for Two Sum.
    # Memory Usage: 14.9 MB, less than 65.62% of Python3 online submissions for Two Sum.
    for x in range(0, len(nums)):
        if target - nums[x] in nums[x+1:]:
            y_index = nums[x+1:].index(target - nums[x]) + x + 1
            return [x, y_index]

def find_index(nums, value, exclude_index):
    # find index exclude index
    for x in range(0, len(nums)):
        if nums[x] == value and x != exclude_index:
            return x
