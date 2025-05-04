void update(int* tree, int i, int n) { for(int j = i +1; j <= n; j += j&-j) ++*(tree +j); }
long long query(int* tree, int i)
{
    int sum = 0;
    for(int j = i +1; 0 <j; j -= j&-j) sum += *(tree +j);
    return sum;
}