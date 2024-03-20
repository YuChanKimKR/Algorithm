#include <stdio.h>

int main() {

    int arr[10];
    int max = 0;
    int num = 0;
    
    for(int i = 0; i < 10; i++){
        scanf("%d\n", &arr[i]);
    }

    for(int i = 0; i < 10; i++) {
        if(arr[i] > max){
                max = arr[i];
                num = i;
            }
    }

    printf("%d\n%d", max, num+1);

    return 0;
}