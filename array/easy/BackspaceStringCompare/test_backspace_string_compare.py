from backspace_string_compare import Solution


def test_solution():

    so = Solution()
    s = "ab#c"
    t = "ad#c"
    ret = so.backspaceCompare(s, t)

    assert ret == True

    s = "ab##"
    t = "c#d#"
    ret = so.backspaceCompare(s, t)

    assert ret == True

    s = "a#c"
    t = "b"
    ret = so.backspaceCompare(s, t)

    assert ret == False
