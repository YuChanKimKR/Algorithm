#include <stdio.h>

int main() {
    int n;
    int arr[10];

    for(int i = 0; i < 10; i++) {
        scanf("%d", &n);
        arr[i] = n % 42;
    }

    int cnt = 0;

    for(int i = 0; i < 10; i++) {
        int is_unique = 1;
        for(int j = 0; j < i; j++) {
            if(arr[i] == arr[j]) {
                is_unique = 0;
                break;
            }
        }
        if(is_unique)
            cnt++;
    }

    printf("%d", cnt);

    return 0;
}