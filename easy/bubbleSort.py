def bubbleSort(source):
    length = len(source)
    print(length)
    for i in range(0,length):
        flag = 0
        for j in range(0,length-1-i):
            ## i mean tail i is max.
            if source[j] > source[j+1]:
                tmp = source[j]
                source[j] = source[j+1]
                source[j+1] = tmp
                flag = -1 
            print("i = {} j = {} j+1 = {} source = {} flag = {}".format(i,j,j+1,source,flag))
        if flag == -1:
            flag = 0
        elif flag == 0:
            ## if no swap , then break
            break
    
    print(source)

def main():
    source = [5,3,2,1,6,4]
    bubbleSort(source)


if __name__=='__main__':
    main()