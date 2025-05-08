

long long recursiveFastex(int b, long long e)
{
    if(!e) return 1;
    long long r = fastex(b,e >>1);
    return (e &1 ? r*r*b : r*r) %1000000007;
}


long long iterativeFastex(long long b, long long e)
{
    long long r = 1;

    for(; e; e >>= 1)
    {
        if(e &1) r = b*r;
        b = b*b;
    }
    return r;
}

