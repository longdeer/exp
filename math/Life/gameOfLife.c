

void gameOfLife(int** board, int r, int* c)
{
    int x,y;
    int X,Y;
    int surv;

    for(x = 0; x <r; ++x)
        for(y = 0; y <*c; ++y)
        {
            surv = 0;

            X = x +1; Y = y -1; if(-1 <X && X <r && -1 <Y && Y <*c) surv += *(*(board +X) +Y) &1;
            X = x +1; Y = y +1; if(-1 <X && X <r && -1 <Y && Y <*c) surv += *(*(board +X) +Y) &1;
            X = x -1; Y = y -1; if(-1 <X && X <r && -1 <Y && Y <*c) surv += *(*(board +X) +Y) &1;
            X = x -1; Y = y +1; if(-1 <X && X <r && -1 <Y && Y <*c) surv += *(*(board +X) +Y) &1;
            X = x +1; Y = y;    if(-1 <X && X <r && -1 <Y && Y <*c) surv += *(*(board +X) +Y) &1;
            X = x -1; Y = y;    if(-1 <X && X <r && -1 <Y && Y <*c) surv += *(*(board +X) +Y) &1;
            X = x; Y = y +1;    if(-1 <X && X <r && -1 <Y && Y <*c) surv += *(*(board +X) +Y) &1;
            X = x; Y = y -1;    if(-1 <X && X <r && -1 <Y && Y <*c) surv += *(*(board +X) +Y) &1;

            if(
                ((surv == 2 || surv == 3) && *(*(board +x) +y) &1)
                ||
                (surv == 3 && ~*(*(board +x) +y) &1)
            )   *(*(board +x) +y) += 2;
        }
    for(x = 0; x <r; ++x)
        for(y = 0; y <*c; ++y)
            *(*(board +x) +y) /= 2;
}

