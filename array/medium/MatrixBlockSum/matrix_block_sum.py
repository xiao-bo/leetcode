from typing import List
import numpy as np


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        # brute method exceeds time limit

        m = len(mat)
        n = len(mat[0])
        # initalized ret

        mat = np.array(mat)
        ret = [[0 for i in range(n)] for j in range(m)]

        '''
        for i in range(m):
            for j in range(n):
                rc_list = self.__get_rc_list(mat, i, j, k)
                ret[i][j] = sum(rc_list)

        return ret
        '''
        # 換個思路想，題目就是在找自己周遭k格的總和
        # time complexity is O(mn*mn)
        # Runtime: 714 ms, faster than 14.81% of Python3 online submissions for Matrix Block Sum.
        # Memory Usage: 33.2 MB, less than 6.03% of Python3 online submissions for Matrix Block Sum.

        for i in range(m):
            for j in range(n):
                row_start = i - k
                if row_start < 0:
                    row_start = 0

                col_start = j - k
                if col_start < 0:
                    col_start = 0

                row_end = i+k+1
                col_end = j+k+1

                ret[i][j] = np.sum(mat[row_start:row_end, col_start:col_end])

        return ret

    def __get_rc_list(self, mat, i, j, k):

        rc_list = []

        for r in range(i-k, i+k+1):
            if r >= 0:  # valid position
                for c in range(j-k, j+k+1):
                    if c >= 0:  # valid position
                        try:
                            print(f'r = {r}, c = {c}')
                            rc_list.append(mat[r][c])
                        except:
                            print(f'valid r = {r}, c= {c}')
                            continue

        return rc_list
