

// Leetcode Q743. Network Delay Time
// You are given a network of n nodes, labeled from 1 to n.
// You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
// and wi is the time it takes for a signal to travel from source to target.
// We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
// If it is impossible for all the n nodes to receive the signal, return -1.


int networkDelayTime(int** times, int timesSize, int* timesColSize, int n, int k)
{
	int* costs = malloc(sizeof(int) *(n +1));
	int  u,v,w,c,i,j,r;

	for(i = 1; i <= n; ++i) *(costs +i) = INT_MAX; *(costs +k) = 0;
	for(i = 1; i <= n -1; ++i)
	{
		r = false;
		for(j = 0; j <timesSize; ++j)
		{
			u = **(times +j);
			v = *(*(times +j) +1);
			w = *(*(times +j) +2);
			c = *(costs +u) == INT_MAX ? INT_MAX : *(costs +u) +w;

			if(c <*(costs +v))
			{
				*(costs +v) = c;
				r = true;
			}
		}
		if(!r) break;
	}
	c = 0;
	for(i = 1; i <= n; ++i)
		if(*(costs +i) == INT_MAX)
		{
			c = -1;
			break;
		}
		else c = *(costs +i) <c ? c : *(costs +i);

	free(costs);
	costs = NULL;

	return c;
}

