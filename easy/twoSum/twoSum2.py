import timeit
def get_two_sum(nums, target):

    if len(nums) < 2:
        return []
    '''
    # Method1: brute method after work 1 years
    # Runtime: 4016 ms, faster than 24.64% of Python3 online submissions for Two Sum.
    # Memory Usage: 14.6 MB, less than 98.26% of Python3 online submissions for Two Sum.
    # time complexity = O(n^2)
    for x in range(0, len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]
    '''

    # Method2: list method by using index
    # Runtime: 640 ms, faster than 37.63% of Python3 online submissions for Two Sum.
    # Memory Usage: 14.7 MB, less than 98.26% of Python3 online submissions for Two Sum.
    # time complexity = O(n^2)
    '''
    for x in range(0, len(nums)):
        print(nums[x + 1:])
        if target - nums[x] in nums[x+1:]:
            y_index = find_index(nums, target - nums[x], x)
            return [x, y_index]
    '''
    
    # Method3: reduce list method time complexity 
    # Runtime: 640 ms, faster than 37.63% of Python3 online submissions for Two Sum.
    # Memory Usage: 14.9 MB, less than 65.62% of Python3 online submissions for Two Sum.
    # time complexity = O(n^2)

    '''
    for x in range(0, len(nums)):
        if target - nums[x] in nums[x+1:]:
            y_index = nums[x+1:].index(target - nums[x]) + x + 1
            return [x, y_index]
    '''

    # Method4: using hash table
    # Runtime: 52 ms, faster than 96.07% of Python3 online submissions for Two Sum.
    # Memory Usage: 15.3 MB, less than 41.02% of Python3 online submissions for Two Sum.
    # time complexity = O(n)
    hash_table = {}
    for x in range(0,len(nums)):
        hash_table[nums[x]] = x 

    for x in hash_table:
        if target - x in hash_table:
            x_index = nums.index(x)
            tmp = nums[x_index] 
            nums[x_index] = 'tmp'
            try:
                y_index = nums.index(target - x)
                nums[x_index]=tmp 
                return [x_index, y_index]
            except:
                continue


def find_index(nums, value, exclude_index):
    # find index exclude index
    for x in range(0, len(nums)):
        if nums[x] == value and x != exclude_index:
            return x
