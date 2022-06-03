from build_array import Solution


def test_solution():
    s = Solution()

    nums = [0, 2, 1, 5, 3, 4]

    expected_result = [0,1,2,4,5,3] 
    ret = s.buildArray(nums)

    assert ret == expected_result

    nums = [5,0,1,2,3,4]
    expected_result = [4,5,0,1,2,3]

    ret = s.buildArray(nums)

    assert ret == expected_result
