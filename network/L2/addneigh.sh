### manage ARP cache
### params:
### $1 - log file path string
### $2 - device name string








loggy=$1
devname=$2








addneigh()
# $1 - host name string
# $2 - host ip4 string
# $3 - host MAC string
{
	echo "caching $1 at $3" >> $loggy

	neighmac=$(echo $3 | sed -e s/-/:/g)
	neightry=$(ip neigh add $2 lladdr $neighmac nud permanent dev $devname 2>&1)

	if		[[ $neightry == "" ]]; then echo "adding done" >> $loggy
	elif	[[ $neightry == "RTNETLINK answers: File exists"* ]]; then

		neightry=$(ip neigh replace $2 lladdr $neighmac nud permanent dev $devname 2>&1)

		if		[[ $neightry == "" ]]; then echo "replacing done" >> $loggy
		else	echo $neightry >> $loggy
		fi

	else	echo $neightry >> $loggy
	fi
}







