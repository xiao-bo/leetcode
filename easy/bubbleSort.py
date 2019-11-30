def bubbleSort(source):
    length = len(source)
    print(length)
    for i in range(0,length):
        for j in range(0,length-1-i):
            if source[j] > source[j+1]:
                tmp = source[j]
                source[j] = source[j+1]
                source[j+1] = tmp
            print("j = {} j+1 = {} source = {}".format(j,j+1,source))
            
    
    print(source)

def main():
    source = [3,4,2,1]
    bubbleSort(source)


if __name__=='__main__':
    main()