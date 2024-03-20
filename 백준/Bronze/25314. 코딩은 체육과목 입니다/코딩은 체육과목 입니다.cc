#include <stdio.h>

int main() {
    int x;
    scanf("%d", &x);
    int y = x / 4;

    if (x % 4 == 0){
        for(int i=0; i<y; i++){
            printf("long ");
        }
    }

    printf("int");

    return 0;
}