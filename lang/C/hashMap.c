struct hashMap { int* K; int* V; int S; };
struct hashMap* init(int size)
{
    struct hashMap* newMap = (struct hashMap*)malloc(sizeof(struct hashMap));

    newMap->K = (int*)calloc(size,sizeof(int));
    newMap->V = (int*)calloc(size,sizeof(int));
    newMap->S = size;

    return newMap;
}
int find(struct hashMap* map, int K)
{
    int i = K % map->S;

    while(*(map->K +i) != 0 && *(map->K +i) != K) i = (i +1) % map->S;

    *(map->K +i) = K;
    return i;
}