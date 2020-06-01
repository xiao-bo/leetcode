#include<stdlib.h>
#include<stdio.h>

void insertion_sort(int nums[],int length){
    for(int i = 1 ; i < length; i++){
        int tmp = nums[i];
        int j = i - 1;
        while(tmp < nums[j] && j >= 0){
            nums[j+1] = nums[j];
            j --;
        }
        nums[j+1] = tmp;
    }
}

void print_all(int nums[],int length){
    for(int i = 0; i < length; i++){
        printf("%d ",nums[i]);
    }
    printf("\n");
}

int main(void){
    int nums[6] = {5,3,1,2,6,4};
    print_all(nums,6);
    insertion_sort(nums,6);
    print_all(nums,6);
}