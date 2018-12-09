#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int checkPalindromic(char *input){
    //printf("%s \n",input);
    int len = strlen(input);
    int ans = 0;
    for(int i = 0, j = len-1; i <len/2;i++,j--){
        if(input[i]==input[j]){
            //printf("i = %d, j=%d continue\n",i,j);
            continue;
        }else{
            //printf("input is not palindromic\n");
            
            return ans;
            
        }
    }
    ans = 1;
    return ans;
}

char* longestPalindrome(char* input) {
    //char ans[1000];

    int len = strlen(input);
    
    int newSize = strlen(input)  + 1; 
    char *longest= (char *)malloc(newSize);
    
    memcpy(longest,&input[0],1);
    
    //char longest[10000];
    //memcpy(longest,&input[0],1);
    //longest[1]='\0';

    for(int head =0;head<len;head++){
        char tmp[10000];
        memcpy(tmp,&input[head],1);
        tmp[1]='\0';
        //printf("head = %d tmp = %s strlen(tmp) = %lu longest = %s \n ",head,tmp,strlen(tmp),longest);

        for (int i = head+1;i<len;i++){
            memcpy(tmp,&input[head],i+1-head);
            tmp[i+1-head]='\0';
            
            if(checkPalindromic(tmp)==1){
                //printf("head = %d i = %d tmp = %s continue\n",head,i,tmp);

                if(strlen(tmp)>strlen(longest)){
                    memcpy(longest,tmp,strlen(tmp)+1);
                    //printf(">> tmp = %s strlen(tmp) = %lu\n ",tmp,strlen(tmp));
                }
                
            }
            /*
            else {
                printf("head = %d i = %d tmp = %s break\n",head,i,tmp);
            }
            */
            
        }
        //printf("head = %d longest = %s\n",head,longest);
        
    }
    int lenx = strlen(longest);
    char *ans= (char *)malloc(lenx);

    for(int i =0;i<lenx;i++){
        ans[i]=longest[i];
    }

    len = strlen(ans);
    printf("ans = %s\n len = %d\n ",ans,lenx);
    ans[len]='\0';
    printf("%c \n",ans[lenx]);
    return ans;
    
}
int main(){
    char *input = "dddddddd";

    char *ans = longestPalindrome(input);
    
    //ans = checkPalindromic(input);
    //checkPalindromic(input);
    printf("ans =%s\n",ans);
}

