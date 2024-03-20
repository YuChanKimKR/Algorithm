#include <stdio.h>

int main() {
    int numbers, cnt = 0;
    int x = 0;
    int arr[10001];
    int xx = 0;
    
    scanf("%d %d", &numbers, &x); 
    
    for (int i = 0; i < numbers; i++) {
        scanf("%d", &arr[i]);
    }
    
    for (int i = 0; i < numbers; i++) {
        if (arr[i] < x){
            xx = arr[i];
            printf("%d ", xx);
        }
    }

    return 0;
}