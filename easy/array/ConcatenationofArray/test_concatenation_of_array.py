from concatenation_of_array import Solution


def test_solution():
    s = Solution()
    nums = [1, 2, 1]
    ret = s.getConcatenation(nums)

    expected_result = [1, 2, 1, 1, 2, 1]

    assert ret == expected_result

    nums = [1, 3, 2, 1]
    ret = s.getConcatenation(nums)

    expected_result = [1, 3, 2, 1, 1, 3, 2, 1]

    assert ret == expected_result
