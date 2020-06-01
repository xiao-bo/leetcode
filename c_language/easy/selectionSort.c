#include<stdlib.h>
#include<stdio.h>

void selection_Sort(int nums[],int length){
    
    for(int i = 0; i < length; i++){
        int minValue = nums[i];
        int minIndex = i;
        for(int j = i+1 ; j < length; j++){
            if (nums[j] < minValue){
                minValue = nums[j];
                minIndex = j;
            }
            
        }
        int tmp = nums[i];
        nums[i] = nums[minIndex];
        nums[minIndex] = tmp;
    }
}

void print_all(int nums[], int length){
    for(int i = 0 ; i < length; i++){
        printf("%d ", nums[i]);
    }
    printf("\n");
}

int main(void){
    int nums[6] = {0,3,1,2,6,4};
    print_all(nums,6);
    selection_Sort(nums,6);
    print_all(nums,6);
}