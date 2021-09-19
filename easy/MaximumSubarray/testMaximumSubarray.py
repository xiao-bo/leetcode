from MaximumSubarray import Solution


def test_soultion():
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4] 
    expected_result = 6
    result = s.maxSubArray(nums)

    assert expected_result == result

    nums = [1]
    expected_result = 1
    result = s.maxSubArray(nums)

    assert expected_result == result 

    nums = [5,4,-1,7,8]
    expected_result = 23
    result = s.maxSubArray(nums)

    assert expected_result == result 
    
    nums = [-1, -2, -3, -4]
    expected_result = -1
    result = s.maxSubArray(nums)

    assert expected_result == result

    nums = [-2, 1]
    expected_result = 1
    result = s.maxSubArray(nums)
    assert expected_result == result

    nums = [-1, 0, -2]
    expected_result = 0
    result = s.maxSubArray(nums)
    assert expected_result == result

    nums = [1,2,3]
    expected_result = 6
    result = s.maxSubArray(nums)
    assert expected_result == result