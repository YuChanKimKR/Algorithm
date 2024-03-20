#include <stdio.h>

int main() {
    int numbers[31];

    for(int i = 1; i <= 30; i++) {
        scanf("%d", &numbers[i]);
    }

    int missing_numbers[2] = {0};
    int count = 0;

    for (int j = 1; j <= 30 && count < 2; j++) {
        int found = 0;

        for(int i = 1; i <= 30; i++) {
            if(j == numbers[i]) {
                found = 1;
                break;
            }
        }

        if(!found) {
            missing_numbers[count++] = j;
        }
    }

    if(missing_numbers[0] > missing_numbers[1]) {
        int temp = missing_numbers[0];
        missing_numbers[0] = missing_numbers[1];
        missing_numbers[1] = temp;
    }

    printf("%d\n%d", missing_numbers[0], missing_numbers[1]);

    return 0;
}