class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows <1:
            return []
        elif numRows == 1:
            return [1]
        elif numRows == 2:
            return [[1],[1,1]]
        elif numRows > 2:
            res = self.generate(numRows-1)             
            ans = [1]

            for x in range(0,numRows-2):
                ans.append(res[numRows-2][x]+res[numRows-2][x+1])
            
            ans.append(1)
            res.append(ans)
            
        
        return res

def main():
    a = Solution()
    print(a.generate(6))

if __name__ == '__main__':
    main()