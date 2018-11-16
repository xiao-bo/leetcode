// this is brute force method

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char* appendCharToCharArray(char* array, char *a){
    int newSize = strlen(array)  + strlen(array) + 1; 
    char *newBuffer = (char *)malloc(newSize);

    // do the copy and concat
    strcpy(newBuffer,array);
    strcat(newBuffer,a); 
    
    array = newBuffer;
    
    
    return array;
}
int checkInString(char *input,char c){
    int len = strlen(input);
    for (int i = 0;i<len;i++){
        if(input[i]==c){
            //printf("is in\n");
            return 1;
        }else{
            //printf("no, it is not in string\n");
            continue;
        }
    }
    return 0;
}
int lengthOfLongestSubstringByBruteForce(char *input) {

    
    int len = strlen(input);
    
    
    

    char str[1000000];
    
    char longest[10000];
    
    
    //input = appendCharToCharArray(input,a);

    memcpy(str,&input[0],len);
    str[len]='\0';
    
    memcpy(longest,&input[0],1);
    longest[1]='\0';
    
    //printf("str = %s\n",str);
    //printf("longest =%s\n",longest);
    //printf("str[1] = %c\n",str[1]);
    
    for (int head = 0;head<len;head++){
        // initial tmp = input[head]
        // it is mean that head flag move to next location and try to find
        // longest substring
        char tmp[10000];
        memcpy(tmp,&input[head],1);
        tmp[1]='\0';

        //printf("head %d: \n ",head);

        for (int i =head+1;i<len;i++){
            // check str[i] is in tmp? if yes, it is repeat. 
            // if no, it is longer
            if(checkInString(tmp,str[i])==0){

                //printf("str[%d] = %c is not in tmp : %s\n",i,str[i],tmp);
                memcpy(tmp,&str[head],i+1-head);
                tmp[i+1-head]='\0';
                //printf("tmp = %c  %c  %s\n",tmp[1],tmp[2],tmp);
                
                
            }else{ // equal
                //printf("str[%d]=%c is in tmp : %s\n",i,str[i],tmp);
                break;
                
            }
            
        }
        // check current substring with current head is longer than old longest?
        if(strlen(tmp)>strlen(longest)){
            memcpy(longest,tmp,strlen(tmp)+1);
        }
        
    }
    

    printf("longest = %s ans = %lu \n",longest,strlen(longest));
    
    return strlen(longest);
}


int main(void){

    //printf("sss\n");
    char* input ="wobgrovw";
    int ans = lengthOfLongestSubstring(input);
    printf("ans = %d", ans);
}