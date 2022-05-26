from threeSum_2021 import Solution

def testThreeSum():

    s = Solution()

    nums = [-1,0,1,2,-1,-4]
    expected_result = [[-1,-1,2],[-1,0,1]]
    result = s.threeSum(nums)

    # 先檢查數量，以免兩邊長度不一
    assert len(result) == len(expected_result)

    for x in expected_result:
        if x in result:
            continue
        else:
            assert x == 0
    

    nums = []
    expected_result = []
    result = s.threeSum(nums)

    assert expected_result == result

    nums = [0]
    expected_result = []
    result = s.threeSum(nums)

    assert expected_result == result

