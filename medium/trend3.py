from itertools import combinations 
def solution(A):
    # write your code in Python 3.6
    
    #print(list(comb))
            
    for longest in range(len(A),1,-1):
        #from biggest subset to smallest subset
        comb = list(combinations(A,longest))
        for subset in comb:
            res = subset[0]
            for element in subset:
                res = res & element
                if res == 0:
                   # the product of subset is 0
                   break
            if res != 0:
               return longest
    return 0

def main():
    a =  [13, 7, 2, 8, 3]
    #a = [1,2,4,8]
    #a = [16,16]
    ans = solution(a)
    print("ans = {}".format(ans))

if __name__ == '__main__':
    main()