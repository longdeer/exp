public int gcd(int a, int b) {
    int rem;

    if(a == 1 || b == 1) return 1;
    while(b != 0) {

        rem = a %b;
        a = b;
        b = rem;
    }
    return  a;
}