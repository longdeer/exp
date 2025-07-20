from scapy.all	import Ether
from scapy.all	import sendp
from scapy.all	import IP
from scapy.all	import UDP
from scapy.all	import Raw
from binascii	import unhexlify








if	__name__ == "__main__":

	packet = unhexlify(

		"ffffffffffff"
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
		"6c4b905b870d"	# target MAC address
	)
	sendp(
		[
			Ether(dst="ff:ff:ff:ff:ff:ff")
			/IP(dst="255.255.255.255")
			/UDP(sport=32677, dport=9)
			/Raw(load=packet)
		]
	)







