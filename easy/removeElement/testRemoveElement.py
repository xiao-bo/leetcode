
from removeElement import Solution

def test_removeElement():
    nums = [3,2,2,3]
    val = 3
    expected_result = [2,2]
    s = Solution()
    res_val, res_nums = s.removeElement(nums, val)
    nums.sort()
    assert res_val == len(expected_result)
    for i in range(0, res_val):
        assert res_nums[i] == expected_result[i]

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    expected_result = [0,0,1,4,3]
    nums.sort()
    res_val, res_nums = s.removeElement(nums, val)
    assert res_val == len(expected_result)
    for i in range(0, res_val):
        assert res_nums[i] == expected_result[i]
        print(i)

    nums = [0,1,2,2,3,3,4,4]
    val = 4
    expected_result = [0,1,2,2,3,3]
    res_val, res_nums = s.removeElement(nums, val)
    assert res_val == len(expected_result)
    for i in range(0, res_val):
        assert res_nums[i] == expected_result[i]
        print(i)

    nums = [2]
    val = 3
    expected_result = [2]
    nums.sort()
    res_val, res_nums = s.removeElement(nums, val)
    assert res_val == len(expected_result)
    for i in range(0, res_val):
        assert res_nums[i] == expected_result[i]

    nums = [1]
    val = 1
    expected_result = []
    nums.sort()
    res_val, res_nums = s.removeElement(nums, val)
    assert res_val == 0
    for i in range(0, res_val):
        assert res_nums[i] == expected_result[i]

    nums = [3,3]
    val = 3
    expected_result = []
    nums.sort()
    res_val, res_nums = s.removeElement(nums, val)
    assert res_val == 0
    for i in range(0, res_val):
        assert res_nums[i] == expected_result[i]

