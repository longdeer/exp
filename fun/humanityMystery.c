

int i = 5;
i = ++i + ++i;		// What "i" equals??
printf("i = %i",i);	// It's 14 (gcc 14 using the gnu11 standard)

