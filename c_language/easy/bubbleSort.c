#include<stdio.h>
#include<stdlib.h>

void bubble_sort(int nums[],int length){

    int tmp = 0;
    for(int i = 0; i < length; i ++){


        for (int j = 0 ; j < length-1-i; j++){
            if (nums[j] > nums[j+1]){
                tmp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = tmp; 
            } 
        }
    }
}

void print_all(int nums[], int length){

    for(int i =0; i < length; i++){
        printf("%d ",nums[i]);
    }
    printf("\n");
}

int main(void){
    int nums[8] = {24};
    print_all(nums,8);
    bubble_sort(nums,8);
    print_all(nums,8);
}