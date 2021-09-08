from RemoveDuplicatesFromSortedArray import Solution


def test_solution():
    s = Solution()
    nums = [1, 1, 2]
    expected_result = [1, 2]
    expected_k = 2

    res_k, res_nums = s.removeDuplicates(nums)

    assert res_k == expected_k
    for i in range(0,res_k):
        assert res_nums[i] == expected_result[i]    

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_result = [0, 1, 2, 3, 4]
    expected_k = 5

    res_k, res_nums = s.removeDuplicates(nums)

    assert res_k == expected_k
    for i in range(0,res_k):
        assert res_nums[i] == expected_result[i]

    nums = [1, 2]
    expected_result = [1, 2]
    expected_k = 2

    res_k, res_nums = s.removeDuplicates(nums)

    assert res_k == expected_k
    for i in range(0,res_k):
        assert res_nums[i] == expected_result[i]

    nums = [0,0,0,0,0,1,2,2,3,3,4,4]
    expected_result = [0,1,2,3,4]
    assert res_k == expected_k
    for i in range(0,res_k):
        assert res_nums[i] == expected_result[i]
 