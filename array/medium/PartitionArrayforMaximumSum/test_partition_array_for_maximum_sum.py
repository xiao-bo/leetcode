from partition_array_for_maximum_sum import Solution


def test_maxSumAfterPartitioning():
    s = Solution()

    arr = [1,15,7,9,2,5,10]
    k = 3
    ret = s.maxSumAfterPartitioning(arr, k)


    assert ret == 84

    arr = [1,4,1,5,7,3,6,1,9,9,3]
    k = 4
    ret = s.maxSumAfterPartitioning(arr, k)

    assert ret == 83

    arr = [1]
    k = 1
    ret = s.maxSumAfterPartitioning(arr, k)

    assert ret == 1