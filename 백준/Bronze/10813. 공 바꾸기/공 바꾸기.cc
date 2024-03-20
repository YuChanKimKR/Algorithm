#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    int arr[101];

    for(int i = 1; i <= n; i++) {
        arr[i] = i;
    }

    for(int k = 0; k < m; k++) {
        int i, j;
        scanf("%d %d", &i, &j);

        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    for(int i = 1; i <= n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}