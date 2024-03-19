#include <stdio.h>

int main() {
	int a, b, time;
	scanf("%d %d %d", &a, &b, &time);

	a += time / 60;
	b += time % 60;

	if (b >= 60) {
		++a;
		b -= 60;
	}

	if (a >= 24) {
		a -= 24;
	}

	printf("%d %d\n", a, b);
	return 0;
}