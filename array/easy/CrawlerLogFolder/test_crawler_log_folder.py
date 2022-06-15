from crawler_log_folder import Solution

def test_crawler_log_folder():
    s = Solution()

    logs = ["d1/","d2/","../","d21/","./"]
    expected_result = 2

    ret = s.minOperations(logs)

    assert ret == expected_result

    logs = ["d1/","d2/","./","d3/","../","d31/"]

    expected_result = 3 

    ret = s.minOperations(logs)

    assert ret == expected_result

    logs = ["d1/","../","../","../"]

    expected_result = 0


    ret = s.minOperations(logs)

    assert ret == expected_result