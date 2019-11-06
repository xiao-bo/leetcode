class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        print("===")
        print("===")
        n = len(matrix)-1
        tmp = []
        for x in range(0,len(matrix)):
            tmp.append(matrix[x][n])
        
        print(tmp)
        
        for x in range(len(matrix)): 
            for y in range(0,x+1): 
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y] 
        print(matrix)
        for r in range(len(matrix)): 
            matrix[r].reverse()
        #print(matrix)

        #matrix[0][n]= tmp

def main():
    a = Solution()
    b = matrix = [
                [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]
             ]
    matrix[:] = zip(*matrix[::-1])
    print(matrix)
    #b[:] = [row[i] for row in b[::-1]]
    #print (b)
    c = 3
    d = 100
    c = ~d
    print(c)
    #print(zip(*matrix[::-1]))
    #a.rotate(matrix)
    #print(matrix)

if __name__ == '__main__':
    main()