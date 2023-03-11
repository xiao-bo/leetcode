class Solution:
    def reverseBits(self, n: int) -> int:
        # method1 using reverse string to solve it
        #  Runtime64 ms Beats 41.85% Memory13.8 MB Beats 95.7% 
        s = '{0:032b}'.format(n)
        res = []
        for i in range(len(s)-1, -1, -1):
            res.append(s[i])
        
        result = ''.join(res)
        return int(result, 2)
