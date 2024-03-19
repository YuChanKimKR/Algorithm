#include <stdio.h>

int main() {
    int value;
    int listNumber;
    int a, b, sum, sum2 = 0;

    scanf("%d", &value);
    scanf("%d", &listNumber);
    for (int i = 0; i < listNumber; i++) {
        scanf("%d %d", &a, &b);
        sum = a * b;
        sum2 += sum;
    }

    if (sum2 == value)
        printf("Yes");
    else
        printf("No");

    return 0;
}
