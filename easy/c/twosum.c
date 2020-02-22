#include<stdio.h>
#include<stdlib.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    
    for (int i = 0; i < numsSize;i++){

        for (int j = i+1; i < numsSize ; i++){
            if ((nums[i]+nums[j]) == target){
                returnSize[0] = i;
                returnSize[1] = j;
            }
        }
    }
    return returnSize;
}

int main(){
    int *nums[4] = {2, 7, 11, 15};
    int len = 4;
    int *ans;
    ans = twoSum(nums,4,9,ans);
    printf("%p",ans);
}
