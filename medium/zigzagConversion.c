#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char* convert(char* inputs, int numRows) {

    int len = strlen(inputs);
    char* ans = (char *)malloc(len);
    int col = 0;
    int row = 0;
    int sum = numRows-1;
    if (numRows <= 1){
        return inputs;
    }
    if (len == 0){
        return "";
    }
    for(int i =0;i<len;i++){
        if(col != 0){
            if (row == 0){
                
                if (col*sum*2>=len){
                    // jump next row
                    printf("jump row = %d, col = %d, i = %d \n",row,col,i);
                    row = row+1;
                    col = 0;
                    i--;
                    continue;
                }
                ans[i] = inputs[col*sum*2];
            }else if(row == sum){
                
                if (col*sum*2+sum>=len){
                    //jump next row
                    printf("jump row = %d, col = %d, i = %d \n",row,col,i);
                    row = row+1;
                    col = 0;
                    i--;
                    continue;
                }
                ans[i] = inputs[col*sum*2+sum];
            }else{
                if (col%2 != 0){
                    
                    if (sum*(col+1)-row>=len){
                        // jump to next row
                        printf("jump row = %d, col = %d, i = %d \n",row,col,i);
                        
                        row = row+1;
                        col = 0;
                        i--;
                        continue;
                    }
                    ans[i] = inputs[sum*(col+1)-row];
                }else if(col%2 ==0 ){
                    
                    if (row+sum*col>=len){
                        // jump to next row
                        printf("jump row = %d, col = %d, i = %d \n",row,col,i);
                        row = row+1;
                        col = 0;
                        i--;
                        continue;
                    }
                    ans[i] = inputs[row+sum*col];
                }
            }
            printf("row = %d, col = %d, i = %d, ans= %c\n",row,col,i,ans[i]);
            col = col+1;

        }else if(col == 0){
            ans[i] = inputs[row];
            printf("row = %d, col = 0, i = %d, ans = %c\n",row,i,ans[i]);
            col = col+1;
        }
        
        
        
    }
    
     
    ans[len] = '\0';
    
    return ans;
}
int main(){
    char *inputs = "0123456789";

    char *ans = convert(inputs,6);
    
    //ans = checkPalindromic(input);
    //checkPalindromic(input);
    printf("ans = %s\n",ans);
}