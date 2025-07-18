

void recursive(char* s,int i, int j)
{
    if(i <j)
    {
        *(s +i) = *(s +i) + *(s +j);
        *(s +j) = *(s +i) - *(s +j);
        *(s +i) = *(s +i) - *(s +j);
        recursive(s,i +1,j -1);
    }
}


void iterative(char* s, int sSize)
{
    int i = 0;
    int j = sSize -1;

    while(i <j)
    {
        *(s +i) += *(s +j);
        *(s +j)  = *(s +i) - *(s +j);
        *(s +i) -= *(s +j);
        ++i;
        --j;
    }
}

