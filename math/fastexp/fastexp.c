long long fastex(int b, long long e)
{
    if(!e) return 1;
    long long r = fastex(b,e >>1);
    return (e &1 ? r*r*b : r*r) %1000000007;
}