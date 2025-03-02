from scapy.all	import sr
from scapy.all	import IP
from scapy.all	import ICMP








def pinger(addr :str, **kwargs) -> str | None :

	"""
		Scapy ICMP ping request.
		Returns input "addr" string in case of successfull pong received.
		Returns None otherwise
	"""

	R = sr(IP(dst=target) /ICMP(), **kwargs)
	if len(R) and len(R[0]): return addr







