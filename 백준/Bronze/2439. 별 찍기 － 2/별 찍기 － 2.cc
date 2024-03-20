#include <stdio.h>

int main() {

    int x;
    scanf("%d", &x);

    for(int j=0; j<x; j++){

        for(int i=x-j-1; i>0; i--){
            printf(" ");
        }

        for(int i=0; i<=j; i++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}