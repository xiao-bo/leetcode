class Solution:
    def reverseWords(self, s: str) -> str:
        # method 1 using O(n) extra space
        # 39ms Beats 56.00% of users with Python3 Memory 16.66 MB Beats 69.74% of users with Python3
        ret = []
        s_input = s.split(' ')
        
        for x in range(len(s_input)-1, -1, -1):
            if s_input[x] == '':
                continue
            ret.append(s_input[x])
        ans = ' '.join(ret)
        return ans
