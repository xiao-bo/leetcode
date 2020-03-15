
def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    longest = 0 
    #hashTable = {}
    checkTable = {}
    for i in range(0,len(A)):
        hashTable = {}
        
        index = i
        if index in checkTable:

          continue
        while True:
           print('i = {} A[{}] = {}'.format(index,index,A[index]))
           if A[index] in hashTable:
               longest = max(len(hashTable),longest)
               print('break')
               break
           else:
               hashTable[A[index]] = 1
               index = A[index]
               checkTable[A[index]] = 1

    return longest

def main():
  a = [5, 4, 0, 3, 1, 6, 2]
  #a = [0,1,2,4,3]
  a = [1,2,3,0,5,6,7,8,4]
  #a = [0,8,7,6,5,4,3,2,1]
  a = [2,3,4,1,0]
  print(solution(a))

if __name__ == '__main__':
  main()