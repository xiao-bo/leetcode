from two_out_of_three import Solution


def test_solution():

    s = Solution()
    nums1 = [1, 1, 3, 2]
    nums2 = [2, 3]
    nums3 = [3]

    ret = s.twoOutOfThree(nums1, nums2, nums3)

    assert sorted(ret) == [2, 3]

    nums1 = [3, 1]
    nums2 = [2, 3]
    nums3 = [1, 2]

    ret = s.twoOutOfThree(nums1, nums2, nums3)

    assert sorted(ret) == [1, 2, 3]

    nums1 = [1, 2, 2]
    nums2 = [4, 3, 3]
    nums3 = [5]
    ret = s.twoOutOfThree(nums1, nums2, nums3)

    assert sorted(ret) == []