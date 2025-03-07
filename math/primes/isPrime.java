public Boolean isPrime(int n) {

    if(n <2) return false;
    if(n == 2 || n == 3) return true;
    if(n%2 == 0 || n%3 == 0) return false;

    int i = 5;
    double j = Math.sqrt(n);

    while(i <= j)
        if(n%i == 0 || n%(i+2) == 0) return false;
        else i += 6;
    return true;
}