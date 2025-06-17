int mathematical(int n)
{
    return n %9 ? n %9 : n ? 9 : n;
}
int recursive(int n)
{
    if(n <10) return n;

    int sum = 0;

    while(n)
    {
        sum += n %10;
        n /= 10;
    }
    return recursive(sum);
}
int iterative(int n)
{
    int current;
    int sum;

    while(9 <n)
    {
        current = n;
        sum = 0;

        while(current)
        {
            sum += current %10;
            current /= 10;
        }
        n = sum;
    }
    return n;
}