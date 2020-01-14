from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str):
        start = []
        
        ## my method
        ## Runtime: 272 ms, faster than 95.52% of Python3 online submissions for Word Search.
        ## Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Word Search.
        if not word:
            return False
        
        ## find start point.
        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if board[row][col] == word[0]:
                    start.append((row,col))
        #print (start)
        
        
        for point in start:
            if self.recursion(board,word[1:],point):
                return True
        return False
        
        
        
    def recursion(self,board:List[List[str]],word:str,start:tuple) :
        row = start[0]
        col = start[1]
        ans = False

        ## save value into tmp
        tmp = board[row][col]
        board[row][col] = '#'
       

        if not word:
            return True

        ## check north
        #print("path = {} word = {} start = {} ans = {}".format(path,word,start,ans))
        if row > 0:
            if board[row-1][col] == word[0]:
                
                ans = ans or self.recursion(board,word[1:],(row-1,col))
        
        ## check south
        if row + 1 < len(board):
            if board[row+1][col] == word[0] :
                
                ans = ans or self.recursion(board,word[1:],(row+1,col))
        
        ## check west
        if col > 0:
            if board[row][col-1]== word[0] :
                
                ans = ans or self.recursion(board,word[1:],(row,col-1))
        
        ## check east
        if col+1 < len(board[0]):
            if board[row][col+1]== word[0]:
                
                ans = ans or self.recursion(board,word[1:],(row,col+1))
        
        ## recovery value 
        board[row][col] = tmp        
        return ans


def test():
    a = Solution()

    testCase = ['SEE','ABCE','SFCS','ASAD','BFDE','CCEEE','CSC']
    testAns =  [ True, True,  True,  True,  True,  False, False]
    for x in range(0,len(testCase)):
        board = [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]
        ans = a.exist(board,testCase[x])
        print(testAns[x])
        print(ans)
        if ans != testAns[x]:
            print("False on {}".format(testCase[x]))
            return False
    return True

def main():
    a = Solution()
    print("123")
    board = [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]
    word = 'BFDE'
    
    board = [['A','A']]
    word = 'AAA'

    board = [['A','A'],['A','A']]
    word = 'AAAA'

    board = [["a","a","a"],
             ["a","b","b"],
             ["a","b","b"],
             ["b","b","b"],
             ["b","b","b"],
             ["a","a","a"],
             ["b","b","b"],
             ["a","b","b"],
             ["a","a","b"],
             ["a","b","a"]]
    word = "aabaaaabbb"

    
    
    #board = [["a",'a','a'],["a",'a','a'],["a",'a','a']]
    #word = 'aaaaaaaaaaaa'
    #board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
    #word = "aaaaaaaaaaaaa"

    #word = 'SEE'
    #word = 'CSC'
    #word = 'ABCE'
    #word = ''
    print(a.exist(board,word))
    print(test())

if __name__ == '__main__':
    main()
