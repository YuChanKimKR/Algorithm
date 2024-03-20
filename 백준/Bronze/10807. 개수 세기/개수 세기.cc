#include <stdio.h>

int main() {
    int numbers, cnt = 0;
    int arr[101];
    
    scanf("%d", &numbers); 
    
    for (int i = 0; i < numbers; i++) {
        scanf("%d", &arr[i]);
    }

    int a;
    scanf("%d", &a);
    
    for (int i = 0; i < numbers; i++) {
        if (arr[i] == a)
            cnt++;
    }
    
    printf("%d", cnt);

    return 0;
}