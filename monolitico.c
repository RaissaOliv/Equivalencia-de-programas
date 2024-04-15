#include <stdio.h>
#include <string.h>

int x;
int num_list[3] = {1,2,3};
int length = sizeof(num_list) / sizeof(num_list[0]);

int main(){
    LOOP:if(x < length){
        if(num_list[x] % 2 == 0) {
            printf("%d e par\n", num_list[x]);
        }
        else {
            printf("%d e impar\n", num_list[x]);
        }
        x += 1;
        goto LOOP;
    }
    return 0;
}