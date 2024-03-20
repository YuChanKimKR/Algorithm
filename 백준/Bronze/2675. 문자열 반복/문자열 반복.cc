#include <stdio.h>
#include <string.h>

int main() {

	int a, b;
	char s[21];

	scanf("%d", &a);

	while (a--) {
		scanf("%d", &b);
		scanf("%s", s);

		for (int i = 0; i < strlen(s); i++) {
			for (int k = 0; k < b; k++) {
				printf("%c", s[i]);
			}
		}
		printf("\n");
	}


	return 0;
}