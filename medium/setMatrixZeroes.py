class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ## space complexity is O(m+n) time complexity is O(m^2n^2). it is too big!!
        ## Runtime: 128 ms, faster than 23.29% of Python online submissions for Set Matrix Zeroes.
        ## Memory Usage: 12.4 MB, less than 43.48% of Python online submissions for Set Matrix Zeroes.
        heigh = len(matrix)
        width = len(matrix[0])
        print(width)
        for x in range(0,heigh):
            for y in range(0,width):
                if matrix[x][y] == 0:
                    for z in range(0,heigh):
                        if matrix[z][y] == 0:
                            continue
                        matrix[z][y] = '1'
                        
                    for z in range(0,width):
                        if matrix[x][z] == 0:
                            continue
                        matrix[x][z] = '1'
                    matrix[x][y] = 0
        print(matrix)
        for x in range(0,heigh):
            for y in range(0,width):
                if matrix[x][y] =='1':
                    matrix[x][y] = 0
def main():
    a = Solution()
    matrix = [
              [1,2,3,4],
              [1,0,1,1],
              [1,1,0,1]
             ]
    matrix = [[1,0],[1,1]]
    matrix = [
              [0,1,2,0],
              [3,4,5,2],
              [1,3,1,5]
              ]
    ans = [[0,0,0,0],
           [0,4,5,0],
           [0,3,1,0]]
    a.setZeroes(matrix)
    print(matrix)

if __name__ == '__main__':
    main()