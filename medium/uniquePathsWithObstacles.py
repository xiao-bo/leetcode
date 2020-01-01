class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        ## Runtime: 28 ms, faster than 88.86% of Python online submissions for Unique Paths II.
        ## Memory Usage: 11.7 MB, less than 84.21% of Python online submissions for Unique Paths II.

        heigh = len(obstacleGrid)
        #print(heigh)
        width = len(obstacleGrid[0])
        #print(width)
        nums = [[ 0 if obstacleGrid[x][y] == 1 else 1 for y in range(width)  ]for x in range(heigh)]
        print(nums)
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[-1][-1] == 1:
            return 0

        for x in range(0,width):
            if nums[0][x] == 0:
                for y in range(x+1,width):
                    nums[0][y] = 0
        for x in range(0,heigh):
            if nums[x][0] == 0:
                for y in range(x+1,heigh):
                    nums[y][0] = 0
                    
        print(nums)
        
        for x in range(1,heigh):
            for y in range(1,width):
                #print(nums[x][y])
                if nums[x][y] == 0:
                    continue
                if nums[x-1][y] == 0:
                    nums[x][y] = nums[x][y-1]
                    #print("false")
                if nums[x][y-1] == 0:
                    nums[x][y] = nums[x-1][y]
                    #print("false")

                nums[x][y] = nums[x-1][y] + nums[x][y-1]
        print(nums)
        return nums[-1][-1]
        
        
def main():
    a = Solution()
    grid = [
              [0,0,0,0],
              [0,1,0,0],
              [0,0,0,0],
           ]
    
    grid = [
            [0,0],
            [1,1],
            [0,0]
            ]
    
    print(a.uniquePathsWithObstacles(grid))

if __name__ == '__main__':
    main()