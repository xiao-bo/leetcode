from running_sum_of_1d_array import Solution


def test_solution():
    s = Solution()
    nums = [1, 2, 3, 4]
    expected_result = [1, 3, 6, 10]
    ret = s.runningSum(nums)

    assert ret == expected_result

    nums = [1, 1, 1, 1, 1]
    expected_result = [1, 2, 3, 4, 5]
    ret = s.runningSum(nums)

    assert ret == expected_result

    nums = [3, 1, 2, 10, 1]

    expected_result = [3, 4, 6, 16, 17]
    ret = s.runningSum(nums)

    assert ret == expected_result
