public int mathematical(int n) {
	return (n -1) %9 +1;
}
public int iterative(int n) {

	int sum;

	while(9 <n) {

		sum = 0;

		while(0 <n) {

			sum += n %10;
			n = (int) Math.floor(n /10);
		}
		n = sum;
	}
	return  n;
}