#!/usr/bin/bash
### manage ARP cache
### params:
### $1 - log file path string








loggy=$1








addneigh()
# $1 - host ip4 string
# $2 - host MAC string
# $3 - host name string
# $4 - interface name string
{
	echo "caching $3 at $2" >> $loggy

	neighmac=$(echo $2 | sed -e s/-/:/g)
	neightry=$(ip neigh add $1 lladdr $neighmac nud permanent dev $4 2>&1)

	if		[[ $neightry == "" ]]; then echo "adding done" >> $loggy
	elif	[[ $neightry == "RTNETLINK answers: File exists"* ]]; then

		neightry=$(ip neigh replace $1 lladdr $neighmac nud permanent dev $4 2>&1)

		if		[[ $neightry == "" ]]; then echo "replacing done" >> $loggy
		else	echo $neightry >> $loggy
		fi

	else	echo $neightry >> $loggy
	fi
}







