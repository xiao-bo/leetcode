from matrix_block_sum import Solution

def test_solution():
    s = Solution()
    '''
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    expected_result = [[12,21,16],[27,45,33],[24,39,28]]
    ret = s.matrixBlockSum(mat, k)

    assert ret == expected_result

    mat = [[1,2,3],[4,5,6],[7,8,9]]
    k = 2
    expected_result = [[45,45,45],[45,45,45],[45,45,45]]
    ret = s.matrixBlockSum(mat, k)

    assert ret == expected_result
    '''
    mat = [[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]]
    k = 3
    expected_result = [[731,731,731],[930,930,930],[930,930,930],[930,930,930],[721,721,721]]
    ret = s.matrixBlockSum(mat, k)

    assert ret == expected_result
