
from decode_string import Solution

def test_decodeString():
    d = Solution()
    '''
    s = "3[a]2[bc]"

    ret = d.decodeString(s)

    assert ret == "aaabcbc"
    
    s = "3[a2[c]]"

    ret = d.decodeString(s)

    assert ret == "accaccacc"

    s = "2[abc]3[cd]ef"

    ret = d.decodeString(s)

    assert ret == "abcabccdcdcdef"

    s = "abc3[cd]xyz"
    ret = d.decodeString(s)

    assert ret == "abccdcdcdxyz"


    s = "100[leetcode]"
    ret = d.decodeString(s)


    assert ret == "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"

    s = "3[z]2[pq]"
    ret = d.decodeString(s)

    assert ret == "zzzpqpq"
    '''
    s = "2[2[y]pq]"
    ret = d.decodeString(s)

    assert ret == "yypqyypq"


    s = "3[z]2[2[y]pq]"
    ret = d.decodeString(s)

    assert ret == "zzzyypqyypq"

    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    ret = d.decodeString(s)

    assert ret == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"


