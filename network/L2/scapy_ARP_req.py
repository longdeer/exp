from scapy.all	import srp
from scapy.all	import Ether
from scapy.all	import ARP
from operator	import getitem








def discoverer(addr, **kwargs) -> str | None :

	"""
		Scapy ARP request.
		Returns string that represents discovered MAC in cause of success.
		Return None otherwise.
	"""

	R = srp(Ether(dst="ff:ff:ff:ff:ff:ff") /ARP(pdst=addr), **kwargs)
	if len(R) and len(R[0]): return getattr(getattr(getitem(getitem(R,0),0),"answer"),"src")







