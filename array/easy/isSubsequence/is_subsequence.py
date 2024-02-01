class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Runtime 41ms Beats 37.61% of users with Python3 
        # Memory 16.62 MB Beats 63.74% of users with Python3
        # by two pointer

        i = 0
        k = 0
        while i < len(s) and k < len(t):
            # 相同時，index都往前
            if s[i] == t[k]:
                i = i + 1
            k = k + 1
            
        # 當t的每一個字元都檢查完，若是s尚未檢查到最後一個字元，代表s不是t的subsequence
        return i == len(s)

