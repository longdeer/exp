int parseInt(char* s)
{
    int parsed = 0;
    int sign = 1;

    for(int i = 0; *(s +i); ++i)
    {
        if(*(s +i) == '-') sign = -1;
        else
        {
            parsed *= 10;
            parsed += *(s +i) -48;
        }
    }
    return  parsed * sign;
}