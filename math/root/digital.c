
int recursive(int num)
{
    if(num <10) return num;

    int sum = 0;

    while(num)
    {
        sum += num %10;
        num /= 10;
    }
    return recursive(sum);
}
int iterative(int num)
{
    int current;
    int sum;

    while(9 <num)
    {
        current = num;
        sum = 0;

        while(current)
        {
            sum += current %10;
            current /= 10;
        }
        num = sum;
    }
    return num;
}