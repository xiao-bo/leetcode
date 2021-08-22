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
    # set 
    set_nums = set(nums)
    for x in nums:
        if target - x in set_nums:
            x_index = get_index(nums, x)
            y_index = get_index(nums, target - x, x_index)
            return [x_index, y_index]

def get_index(nums, x, exclude_index=None):
    for index in range(0, len(nums)):
        if nums[index] == x and index != exclude_index:
            return index