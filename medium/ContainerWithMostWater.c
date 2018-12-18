#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int min(int a, int b){
    if (a>=b){
        return b;
    }else{
        return a;
    }
}
int bruteFroceMaxArea(int* height, int heightSize) {
    int len = sizeof(height);
    int mArea = 0;
    int currentArea = 0;
    int headHeight = 0;
    int tailHeight = 0;
    if (len < 3){
        return 0;
    }
    for(int i = 0 ; i < heightSize ; i++){
        printf("%d\n", height[i]);
        // if height is small head, its area must small head 
        // because width is small origin.
        if(height[i] < headHeight ){
            continue;
        }
        for(int j = heightSize-1 ; j > i ; j--){
            if(height[j] < tailHeight){
                continue;
            }
            currentArea = min(height[i],height[j]) * (j-i);
            printf("height[%d] = %d, height[%d] = %d area = %d\n",i,height[i],j,height[j],currentArea);
            if( currentArea > mArea ){
                mArea = currentArea;
                headHeight = height[i];
                tailHeight = height[j];
            }
            

        }
        
    }
    return mArea;    
}
int dymaicMaxArea(int* height, int heightSize){
    int mArea = 0;
    int currentArea = 0;
    int len = sizeof(height);

    for(int i = 0 ; i < heightSize ; i++){
        for(int j = i+1 ; j < heightSize ; j++){
            currentArea = min(height[i],height[j])*(j-i);
        }
    }

    return mArea;
}

int main(){
    
    //char *input = "3dddddddd";
    int input[] = {1,8,6,2,5,4,8,3,7};
    int ans;
    
    ans = bruteFroceMaxArea(input,9);
    printf("ans %d\n",ans);
    return 0;
}