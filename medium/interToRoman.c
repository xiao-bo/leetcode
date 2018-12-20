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

char* intToRoman(int num) {
    int len = 1000;
    char* ans = (char *)malloc(len);
    int a[4] ={ -1,-1,-1,-1 };
    int NumberOfDigit = 0;
    
    for (int i = 3; i > -1;i--){
        if (num < 10){
            a[i] = num;
            NumberOfDigit ++;
            break;
        }
        a[i] = num % 10;
        num = num / 10;
        NumberOfDigit ++;
    }
    int index = 0;
    for(int i = 0; i < a[0] && a[0] > -1; index++, i++){   
        printf("append M ");
        printf("index = %d\n ",index);
        ans[index] = 'M';
    }

    for(int i = 0 ; i < a[1] && a[1] < 4 && a[1] > -1; i++, index++){
        printf("append C ");
        printf("index = %d\n ",index);
        ans[index] = 'C';
    }
    if(a[1] == 4 && a[1] > -1){
        printf("4 append CD ");
        printf("index = %d\n ",index);
        ans[index] = 'C';
        index++;
        ans[index] = 'D';
        index++;
    }else if(a[1] == 9 && a[1] > -1){
        printf("9 append CM ");
        printf("index = %d\n ",index);
        ans[index] = 'C';
        index ++;
        ans[index] = 'M';
        index++;
    }else if (a[1] >= 5){
        ans[index] = 'D';
        index++;
        if(a[1] > 5 && a[1] < 9 && a[1] > -1){
            for(int i =0;i < (a[1]-5);index++,i++){
                ans[index] = 'C';
            }
        }
    }

    for(int i = 0 ; i < a[2] && a[2] < 4 && a[2] > -1; i++, index++){
        printf("append X ");
        printf("index = %d\n ",index);
        ans[index] = 'X';
    }
    if(a[2] == 4 && a[2] > -1){
        printf("4 append XL ");
        printf("index = %d\n ",index);
        ans[index] = 'X';
        index++;
        ans[index] = 'L';
        index++;
    }else if(a[2] == 9 && a[2] > -1){
        printf("9 append XC ");
        printf("index = %d\n ",index);
        ans[index] = 'X';
        index ++;
        ans[index] = 'C';
        index++;
    }else if (a[2] >= 5){
        ans[index] = 'L';
        index++;
        if(a[2] > 5 && a[2] < 9 && a[2] > -1){
            for(int i =0;i < (a[2]-5);index++,i++){
                ans[index] = 'X';
            }
        }
    }

    for(int i = 0 ; i < a[3] && a[3] < 4 && a[3] > -1; i++, index++){
        printf("append I ");
        printf("index = %d\n ",index);
        ans[index] = 'I';
    }
    if(a[3] == 4 && a[3] > -1){
        printf("4 append IV ");
        printf("index = %d\n ",index);
        ans[index] = 'I';
        index++;
        ans[index] = 'V';
        index++;
    }else if(a[3] == 9 && a[3] > -1){
        printf("9 append IX ");
        printf("index = %d\n ",index);
        ans[index] = 'I';
        index ++;
        ans[index] = 'X';
        index++;
    }else if (a[3] >= 5){
        ans[index] = 'V';
        index++;
        if(a[3] > 5 && a[3] < 9 && a[3] > -1){
            for(int i =0;i < (a[3]-5);index++,i++){
                ans[index] = 'I';
            }
        }
    }
    
    for(int i = 0 ; i < 4 ; i++){
        if (a[i]>-1){
            printf("a[%d] = %d\n",i,a[i]);
        }

    }
    printf("digit = %d ans = %s \n",NumberOfDigit,ans);
    return ans;
}
int main(){
    printf("123\n");
    char *a = intToRoman(88);
    printf("%s",a);
}