public int mathematical(int n) {
	return (n -1) %9 +1;
}
public int logical(int n) {

	int m = n %9;
	if(0 <m) return m;
	if(0 <n) return 9;
	return n;
}
public int recursive(int n) {

	if(n <10) return n;

	int sum = 0;

	while(0 <n) {

		sum += n %10;
		n /= 10;
	}
	return  recursive(sum);
}
public int iterative(int n) {

	int sum;

	while(9 <n) {

		sum = 0;

		while(0 <n) {

			sum += n %10;
			n /= 10;
		}
		n = sum;
	}
	return  n;
}