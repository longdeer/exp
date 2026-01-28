

// Leetcode Q743. Network Delay Time
// You are given a network of n nodes, labeled from 1 to n.
// You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
// and wi is the time it takes for a signal to travel from source to target.
// We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
// If it is impossible for all the n nodes to receive the signal, return -1.


var networkDelayTime = function(times, n, k) {

	var graph = new Array(n +1).fill().map(_ => new Object());
	var costs = new Array(n +1).fill(Infinity);
	costs[k] = 0;
	var pq = [[ 0,k ]];
	var mi;
	var u;
	var v;
	var w;
	var c;

	times.forEach(([ u,v,w ]) => graph[u][v] = w);
	while(pq.length) {

		pq.sort((a,b) => a[0] - b[0]);
		[ c,u ] = pq.shift();

		if(c <= costs[u])
			Array.prototype.forEach.call(Object.keys(graph[u]),v => {

				w = graph[u][v];
				v = Number(v);

				if(c+w <costs[v]) {

					costs[v] = c+w;
					pq.push([ costs[v],v ])
				}
			})
	}
	mi = costs.slice(1).reduce((A,V) => Math.max(A,V));
	return mi === Infinity ? -1 : mi
}

