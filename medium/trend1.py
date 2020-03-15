# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def getSum(i):
    sumDigit = 0
    while i > 0:
        sumDigit = sumDigit + (i % 10)
        i = i / 10
    return sumDigit
def solution(N):
    # write your code in Python 3.6
    if isinstance(N, int)== False:
        return 0

    if N < 1:
        return 0

    sumDigit = getSum(N)

    for x in range(N+1,100005):
        if getSum(x) == sumDigit:
            print(x)
            return x
    return 0
def main():
    N = 28
    print(solution(N))

if __name__ == '__main__':
    main()
