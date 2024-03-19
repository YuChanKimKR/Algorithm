#include <stdio.h>

int main() {

    int Score;
    scanf("%d", &Score);
    
    if(Score <= 100 && Score >= 90)
        printf("A");
    else if(Score <= 89 && Score >= 80)
        printf("B");
    else if(Score <= 79 && Score >= 70)
        printf("C");
    else if(Score <= 69 && Score >= 60)
        printf("D");
    else
        printf("F");

    return 0;
}
