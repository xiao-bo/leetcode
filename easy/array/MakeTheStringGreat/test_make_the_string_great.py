from make_the_string_great import Solution

def test_solution():
    so = Solution()

    s = "leEeetcode"
    ret = so.makeGood(s)

    assert ret == "leetcode"


    s = "abBAcC"
    ret = so.makeGood(s)

    assert ret == ""


    s = "s"
    ret = so.makeGood(s)

    assert ret == "s"

    s = "pP"
    ret = so.makeGood(s)

    assert ret == ""

    s = "Pp"
    ret = so.makeGood(s)

    assert ret == ""


    s = "djrDdRJD"
    ret = so.makeGood(s)

    assert ret == ""