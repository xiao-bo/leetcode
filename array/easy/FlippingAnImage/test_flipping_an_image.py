from flipping_an_image import Solution


def test_solution():
    s = Solution()
    image = [[1,1,0],[1,0,1],[0,0,0]]
    expected_result = [[1,0,0],[0,1,0],[1,1,1]]
    ret = s.flipAndInvertImage(image)

    assert ret == expected_result

    image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    expected_result = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    ret = s.flipAndInvertImage(image)

    assert ret == expected_result