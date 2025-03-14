# python	3.10
# pysmi		0.3.4
# pysnmp	4.4.11
# author: lngd
# lngdeer@gmail.com
from typing								import Any
from typing								import List
from typing								import Dict
from typing								import Tuple
from typing								import Callable
from sys								import exc_info
from time								import time
from asyncore							import loop
from traceback							import format_exception
from pysnmp.entity						import config
from pysnmp.entity.engine				import SnmpEngine
from pysnmp.entity.rfc3413				import ntfrcv
from pysnmp.carrier.asyncore.dgram		import udp
from pysnmp.carrier.asyncore.dispatch	import AsyncoreDispatcher
from pysnmp.smi							import builder
from pysnmp.smi							import view
from pysnmp.smi.rfc1902					import ObjectType
from pysnmp.smi.rfc1902					import ObjectIdentity
from pysnmp.proto.rfc1902				import ObjectName
from pysnmp.proto.rfc1902				import OctetString
from pysnmp.error						import PySnmpError








class AsyncoreDispatcher(AsyncoreDispatcher):

	""" Special version that allows dispatching with timer """

	def runDispatcher(self, kill_timer :int):

		start = time()

		while self.jobsArePending() or self.transportsAreWorking():
			tick = time()

			if		kill_timer <tick - start : break
			try:	loop(self.getTimerResolution(), use_poll=True, map=self.__sockMap, count=1)
			except	KeyboardInterrupt : raise
			except:	raise PySnmpError("poll error: %s"%";".join(format_exception(*exc_info())))

			self.handleTimerTick(tick)








class PySNMPv1Trap:
	def __init__(self):

		self.builder	= builder.MibBuilder()
		self.viewer		= view.MibViewController(self.builder)
		self.handlers	= list()
		self.loaded		= list()

	def __call__(
					self,
					listen_ip		:str,
					listen_port		:int,
					listen_time		:int,
					community		:str,
					community_i		:str,
					trap_callback	:Callable[
						[
							SnmpEngine,
							int,
							OctetString,
							OctetString,
							List[Tuple[ObjectName,Any]]
						],	Dict[
							str,
							List[str]
						]
					]
				):

		# Following is the typical trap example, according to official documentation.
		ENGINE = SnmpEngine()
		ENGINE.registerTransportDispatcher(AsyncoreDispatcher())

		config.addTransport(

			ENGINE,
			udp.domainName + ( 1, ),
			udp.UdpTransport().openServerMode(( listen_ip,listen_port ))
		)

		config.addV1System(ENGINE, community_i, community)
		ntfrcv.NotificationReceiver(ENGINE, trap_callback)

		try:

			ENGINE.transportDispatcher.jobStarted(1)
			ENGINE.transportDispatcher.runDispatcher(listen_time)

		finally:	ENGINE.transportDispatcher.closeDispatcher()


	def add_handler(self, handler :Callable[[Tuple[str,str,str,str,str,str,str]],None]):

		"""
			Helper method for adding external trap data handler.
			Argument "handler" must be callable which must accept, according to "callback", a tuple of:
				SRC		string,
				NMOD	string,
				NSYM	string,
				NIND	string,
				VMOD	string,
				VSYM	string,
				VIND	string.
		"""

		if	callable(handler): self.handlers.append(handler)


	def get_modules(self, sources :List[str], modules :List[str]):

		"""
			Loads MIB modules lists.
			All loaded modules will be accessible by "loaded" attribute.
		"""

		self.builder.addMibSources(*( builder.DirMibSource(S) for S in sources ))
		self.builder.loadModules(*modules)
		module_name	= self.viewer.getFirstModuleName()

		while True:

			if module_name:	self.loaded.append(module_name)
			try:			module_name = self.viewer.getNextModuleName(module_name)
			except:			break


	def callback(
					self,
					engine				:SnmpEngine,
					state_reference		:int,
					context_engine_id	:OctetString,
					context_name		:OctetString,
					bind_variables		:List[Tuple[ObjectName,Any]],
					cbCtx				:Any,
				)-> Dict[str,List[str]]	:

		context = engine.observer.getExecutionContext("rfc3412.receiveMessage:request")
		SRC = context["transportAddress"][0]


		for name, value in bind_variables:

			rfcobj = ObjectType(ObjectIdentity(name), value).resolveWithMib(self.viewer)
			NMOD, NSYM, NIND = rfcobj[0].getMibSymbol()


			# Not shure index is always wrapped in a tupple, just seen it for some traps,
			# the idea it must be stringable otherwise.
			try:	NIND = NIND[0]
			except:	pass


			# Perhaps some impirical data became the base for current extraction,
			# that ObjectIdentity value not always obtainable.
			try:	VMOD, VSYM, VIND = rfcobj[1].getMibSymbol()
			except:	VMOD, VSYM, VIND = str(), str(rfcobj[1]), str()


			# ObjectIdentity value might be some empty tuple and so on, the best idea to
			# convert all to actual trully/galsy strings.
			current = (

				str(SRC),
				str(NMOD), str(NSYM), str(NIND),
				str(VMOD), str(VSYM),
				str(VIND) if VIND else str()
			)


			# At this point all external handlers will be invoked for current trap tuple.
			for handler in self.handlers : handler(current)








if	__name__ == "__main__":


	test = PySNMPv1Trap()
	test.add_handler(lambda *args : [ print(arg) for arg in args ])
	test.get_modules(

		[ "/home/vla/.pysnmp/mibs" ],
		[ "SNMPv2-MIB", "IF-MIB", "SNMP-COMMUNITY-MIB", "XPPC-MIB", "POLYGON-MIB", "POLYCOM740-MIB" ]
	)
	test("127.0.0.18", 54321, 10, "trap", "area", test.callback)







