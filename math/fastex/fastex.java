

public long recursiveFastex(int b, long e) {

    if(e == 0) return 1;
    long r = fastex(b,e >>1)
    return (e%2 == 1 ? r*r*b : r*r)
}


public long fastex(long b, long e) {

    long r = 1;

    while(0 <e) {
        if((e &1) == 1) r = b*r;
        b = b*b;
        e >>= 1;
    }
    return r;
}

