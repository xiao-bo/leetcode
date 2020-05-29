# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(N):
    # write your code in Python 3.6
    pow2 = set([int(math.pow(2,x)) for x in range(0,32)])
    
    s = bin(N).split("b")
    maxLen = 0
    tmp = 0
    
    if N in pow2 or N+1 in pow2:
        return 0
    
    for x in range(1,len(s[1])):
        #print("s[1][{}] = {} ".format(x,s[1][x]))
        if s[1][x] == '1':
            maxLen = max(maxLen,tmp)
            tmp = 0
            continue
        else:
            tmp = tmp + 1
        #print("tmp = {}".format(tmp))
    return maxLen

    
    

def main():
    n = 529
    print(solution(n))


if __name__ == '__main__':
    main()