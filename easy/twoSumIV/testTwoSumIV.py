from twoSumIV import findTarget


def test_findTarget():

    root = [5,3,6,2,4,None,7]
    k = 9

    assert findTarget(root, k) == True

    root = [5,3,6,2,4,None,7]
    k = 28

    assert findTarget(root,k) == False

    root = [2,1,3]
    k = 4

    assert findTarget(root, 4) == True

    assert findTarget(root, 1) == False

    assert findTarget(root, 3) == True