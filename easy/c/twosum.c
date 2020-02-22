#include<stdio.h>
#include<stdlib.h>
int* twoSum(int* nums, int numsSize, int target){
    int *returnSize = (int*)malloc(2*sizeof(int));

    for (int i = 0; i < numsSize;i++){

        for (int j = i+1; j < numsSize ; j++){
            if ((nums[i]+nums[j]) == target){
                returnSize[0] = i;
                returnSize[1] = j;
               
            }
        }
    }
    
    
    return returnSize;
}

int main(){
    int nums[4] = {2, 7, 11, 15};    
    int *ans = twoSum(nums,4,9);
    printf("%d %d",ans[0],ans[1]);
    free(ans);
}
