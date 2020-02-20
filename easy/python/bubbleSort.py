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
def selectionSort(nums):
    for x in range(0,len(nums)):
        minimun = float('inf')
        minIndex = -1
        for y in range(x,len(nums)):
            ##找最小的值
            if nums[y] < minimun:
                minimun = nums[y]
                minIndex = y
        ## 最小的值跟第x個互換，換完代表前x個已經排序好。
        nums[x],nums[minIndex] = nums[minIndex],nums[x]
        print("x = {} nums = {} ".format(x,nums))
        
def insertionSort(nums):
    for x in range(1,len(nums)):
        for y in range(0,x):
            if nums[x] < nums[y]:
                tmp = nums[x]
                for z in range(x,y,-1):
                    nums[z] = nums[z-1]
                    #print("x = {}, y = {} , z = {} nums = {}".format(x,y,z,nums))
                nums[y] = tmp
                break
        print("x = {} nums = {} ".format(x,nums))
def main():
    #source = [5,2,3,1,6,4]
    source = [2,1,5,4,3]
    #bubbleSort(source)
    #selectionSort(source)
    insertionSort(source)

if __name__=='__main__':
    main()