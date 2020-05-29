/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include<stdlib.h>
#include<stdio.h>
int* twoSum(int* nums, int numsSize, int target) {
    
    
    int *ans = (int*)malloc(sizeof(int)*2);

    for(int i = 0; i < numsSize;i++){
        for (int j = 0; j < numsSize;j++){
            if (nums[i]+nums[j] == target){
                printf("i = %d j = %d\n",i,j);
                ans[0] = i;
                ans[1] = j;
                return ans;
            }
        }
    }
    return ans;

}

int main(void){
    int *nums = (int*)malloc(sizeof(int)*4);
    int *ans = (int*)malloc(sizeof(int)*2);

    //nums = {2,7,11,15}
    nums[0] = 2;
    nums[1] = 7;
    nums[2] = 11;
    nums[3] = 15;
    //int *nums = {2, 7, 11, 15};
    int target = 9;
    ans = twoSum(nums,4,target);
    printf("%d %d",ans[0],ans[1]);
    free(nums);
}