#include <stdio.h>

int main() {

    int a=0, b=0, T;
    scanf("%d", &T);

    for(int i=0; i<T; i++){
        scanf("%d %d\n", &a, &b);
        printf("Case #%d: %d\n", i+1, a+b);
    }

    return 0;
}