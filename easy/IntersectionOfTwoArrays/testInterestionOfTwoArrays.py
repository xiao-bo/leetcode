from IntersectionOfTwoArrays import Solution


def test_intersection():
    s = Solution()
    # check null
    nums1 = []
    nums2 = [2,2]
    result = s.intersection(nums1, nums2)
    expected_result = False

    assert result == expected_result

    nums1 = [1,2]
    nums2 = [] 
    result = s.intersection(nums1, nums2)
    expected_result = False

    assert result == expected_result

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    result = s.intersection(nums1, nums2)
    expected_result = [2]

    assert result == expected_result

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    result = s.intersection(nums1, nums2)
    result.sort()
    expected_result = [4,9]

    assert result == expected_result

