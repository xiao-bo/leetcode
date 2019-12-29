class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ## Runtime: 76 ms, faster than 92.52% of Python online submissions for Minimum Path Sum.
        ## Memory Usage: 13.1 MB, less than 17.65% of Python online submissions for Minimum Path Sum.
        h = len(grid)
        w = len(grid[0])
        path = [[0 for x in range(w)]for y in range(h)]
        path[0][0] = grid[0][0]
        print(path)
        print(w)
        
        for x in range(1,w):
            ## compute value of board of top 
            path[0][x] = path[0][x-1] + grid[0][x]
        for x in range(1,h):
            ## compute value of board of left
            path[x][0] = path[x-1][0] + grid[x][0]
      
        for x in range(1,h):
            for y in range(1,w):
                path[x][y] = min(path[x-1][y],path[x][y-1])+grid[x][y]
        
        #path = [[]]
        
        print(path)
        return path[-1][-1]
        
        
def main():
    a = Solution()
    grid = [
              [1,3,1],
              [1,5,1],
              [4,2,1]
            ]

    grid = [
            [1,2,5],
            [3,2,1]
            ]
    print(a.minPathSum(grid))

if __name__ == "__main__":
    main()