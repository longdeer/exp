public long fastex(int b, long e) {

    if(e == 0) return 1;
    long r = fastex(b,e >>1)
    return (e%2 == 1 ? r*r*b : r*r)
}