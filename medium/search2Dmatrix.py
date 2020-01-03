class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ## linear search + binary search
        ## Runtime: 52 ms, faster than 65.16% of Python online submissions for Search a 2D Matrix.
        ## Memory Usage: 13.6 MB, less than 45.24% of Python online submissions for Search a 2D Matrix.
        if not matrix:
            return False
        heigh = len(matrix)
        width = len(matrix[0])
        #print("heigh = {},width = {}".format(heigh,width))
        row = -1
        ## linear search 
        for x in range(0,heigh-1):

            if matrix[x+1][0] > target and target > matrix[x][0]:
                row = x
                #print("matrix[{}+1]= {} >target({}) >matrix[{}]={}".format(x,matrix[x+1][0],target,x,matrix[x][0]))
                break
            elif matrix[x][0] == target or matrix[x+1][0] == target:

                return True
            elif matrix[x][0] > target:
                #print("matrix[{}]={}>target({}) ".format(x,matrix[x][0],target))

                row = x - 1
            elif target > matrix[x][0]:
                #print("target({})>matrix[{}+1]={} ".format(target,x,matrix[x+1][0]))
                continue
        #print("row = {}".format(row))
        if row == -1:
            row = heigh - 1
        
        ## binary search
        left = 0
        right = width - 1
        while left <= right:
            mid = int((left + right)/2)
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
        return False


def test():
    a = Solution()
    matrix = [
                  [2,   4,  5,  7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 40],
                  [52, 57, 59, 61],
                  [66, 68, 71, 73],
                  [82, 87, 91, 93]
            ]
    for row in range(0,len(matrix)):
        for y in range(matrix[row][0],matrix[row][-1]):

            target = y

            ans = a.searchMatrix(matrix,target)
            #print("ans = {} target = {}".format(ans,target))
            '''
            if ans == True:
                continue
            
            if ans != row:
                print("ans = {} false in {} row , target = {}".format(ans,row,y))
                return False
            '''
            groundTruth = (y in matrix[row])
            if ans != groundTruth:
                print("groundTruth = {} ans = {} false in {} row , target = {}".format(groundTruth,ans,row,y))
                return False

    return True
    

def main():
    a = Solution()
    matrix = [
                  [2,   4,  5,  7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 40],
                  #[52, 57, 59, 61],
                  #[66, 68, 71, 73],
                  #[82, 87, 91, 93]
            ]
    target = 11
    target = 13
    target = 7
    #print(a.searchMatrix(matrix,target))
    print(test())
if __name__ == "__main__":
    main()