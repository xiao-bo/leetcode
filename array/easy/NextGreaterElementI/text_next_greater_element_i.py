from next_greater_element_i import Solution


def test_solution():

    s = Solution()

    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    ret = s.nextGreaterElement(nums1, nums2)

    expected_result = [-1,3,-1]

    assert ret == expected_result

    nums1 = [2,4 ]
    nums2 = [1,2,3,4]

    ret = s.nextGreaterElement(nums1, nums2)

    expected_result = [3,-1]

    assert ret == expected_result

    