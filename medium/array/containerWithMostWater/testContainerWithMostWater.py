from containerwithMostWater import Solution


def test_solution():
    s = Solution()
    
    # case1
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    result = s.maxArea(height)
    expected_result = 49

    assert result == expected_result

    # case2
    height = [1, 1]
    result = s.maxArea(height)
    expected_result = 1

    assert result == expected_result

    # case3
    height = [4, 3, 2, 1, 4]
    result = s.maxArea(height)
    expected_result = 16

    assert result == expected_result

    # case4
    height = [1, 2, 1]
    result = s.maxArea(height)
    expected_result = 2

    assert result == expected_result

    # case5
    height = [1, 100, 1]
    result = s.maxArea(height)
    expected_result = 2

    assert result == expected_result
    
    # case6
    height = [1, 100, 100, 1, 1, 1, 1, 1]
    result = s.maxArea(height)
    expected_result = 100

    assert result == expected_result

    # case7
    height = [1, 2, 2, 1, 1, 1]
    result = s.maxArea(height)
    expected_result = 5

    assert result == expected_result

    # case8
    height = [1, 2]
    result = s.maxArea(height)
    expected_result = 1

    assert result == expected_result
