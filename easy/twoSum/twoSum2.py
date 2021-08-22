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
    # hash table
    hash_table = {}
    # nums value is equals hash table value
    for x in range(0, len(nums)):
        hash_table[x] = nums[x]

    print(target)
    print(hash_table)
    for x in hash_table:

        print(x, hash_table[x], target - hash_table[x])
        if target - hash_table[x] in hash_table.values():
            print(list(hash_table.values()).index(target - hash_table[x]))

            return [x, list(hash_table.values()).index(target - hash_table[x])]
        '''
        if (target - x) in hash_table and (hash_table[target - x]!=hash_table[x]):
            print([hash_table[x], hash_table[target-x]])
            return [hash_table[x], hash_table[target-x]]
        '''