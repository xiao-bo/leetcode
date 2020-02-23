class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """       

        if numRows <1:
            return [[1]]
        elif numRows == 1:
            return [[1],[1,1]]
        
        
        elif numRows > 1:
            res = self.generate(numRows-1)             
            ans = [1]

            for x in range(0,numRows-1):
                ans.append(res[numRows-1][x]+res[numRows-1][x+1])
            
            ans.append(1)
            res.append(ans)
            
        
        return res
    def getRow(self,rowIndex):
        ans = self.generate(rowIndex)
        #print (ans[rowIndex])
        return ans[rowIndex]
def main():
    a = Solution()
    print(a.getRow(3))

if __name__ == '__main__':
    main()