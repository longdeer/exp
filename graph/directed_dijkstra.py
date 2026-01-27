

# Leetcode Q743. Network Delay Time
# You are given a network of n nodes, labeled from 1 to n.
# You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
# and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
# If it is impossible for all the n nodes to receive the signal, return -1.


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int :

	graph = defaultdict(dict)
	costs = [ inf ] *(n +1)
	costs[k] = 0 
	pq = [( 0,k )]

	for u,v,w in times: graph[u][v] = w
	while pq:

		cost,u = heappop(pq)

		if	cost <= costs[u]:

			for v,w in graph[u].items():
				if	(current := cost +w) <costs[v]:

					costs[v] = current
					heappush(pq,( current,v ))

	return	max_cost if (max_cost := max(costs[1:])) != inf else -1

