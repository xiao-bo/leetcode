from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = []
        ans = []

        ## my method
        ## Runtime: 264 ms, faster than 95.72% of Python3 online submissions for Word Search.
        ## Memory Usage: 14 MB, less than 95.74% of Python3 online submissions for Word Search.
        
        if not word:
            return False
        
        ## find start point.
        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if board[row][col] == word[0]:
                    start.append((row,col))
        #print (start)
        
        
        for point in start:
            ans.append(self.recursion(board,word[1:],point,'0'))
        #print(ans)
        if True in ans:
            return True
        else:
            return False
        
        
    def recursion(self,board:List[List[str]],word:str,start:tuple,path:str) -> bool:
        row = start[0]
        col = start[1]
        ans = False

        ## save value into tmp
        tmp = board[row][col]
        board[row][col] = False
       

        if not word:
            return True

        ## check north
        #print("path = {} word = {} start = {} ans = {}".format(path,word,start,ans))
        if row > 0:
            if board[row-1][col] == word[0] and path != 'n':
                #print("path = {} word = {} start = {} go north".format(path,word,start))
                ans = ans or self.recursion(board,word[1:],(row-1,col),'s')
        
        ## check south
        if row + 1 < len(board):
            if board[row+1][col] == word[0] and path != 's':
                #print("path = {},word = {} start = {} go south".format(path,word,start))
                ans = ans or self.recursion(board,word[1:],(row+1,col),'n')
        
        ## check west
        if col > 0:
            if board[row][col-1]== word[0] and path != 'w':
                #print("path = {} word = {} start = {} go west".format(path,word,start))
                ans = ans or self.recursion(board,word[1:],(row,col-1),'e')
        
        ## check east
        if col+1 < len(board[0]):
            if board[row][col+1]== word[0] and path != 'e':
                #print("path = {} word = {} start = {} go east".format(path,word,start))
                ans = ans or self.recursion(board,word[1:],(row,col+1),'w')
        
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
        #print(testAns[x])
        #print(ans)
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
    #print(test())

if __name__ == '__main__':
    main()
