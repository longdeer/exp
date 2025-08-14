#!/bin/bash
# Wake if down
# $1 - target ip
# $2 - target MAC (xx:xx:xx:xx:xx:xx)








prob=$(ping -c 1 $1)

if [[ $prob == *"0 received"* ]]; then

	wakeonlan $2
	sleep 100
fi







