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

		self.builder = builder.MibBuilder()
		self.viewer = view.MibViewController(self.builder)

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

		except		Exception as E : print(f"\n\ninner {patronus(E)}")
		finally:	ENGINE.transportDispatcher.closeDispatcher()


	def get_modules(self, sources :List[str], modules :List[str]):

		self.builder.addMibSources(*( builder.DirMibSource(S) for S in sources ))
		self.builder.loadModules(*modules)


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
		responses = { SRC: list() }


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


			print(( str(NMOD), str(NSYM), str(NIND), str(VMOD), str(VSYM), str(VIND) ))
			# responses[SRC].append(( str(NMOD), str(NSYM), str(NIND), str(VMOD), str(VSYM), str(VIND) ))


		return	responses








if	__name__ == "__main__":


	test = PySNMPv1Trap()
	test.get_modules(

		[ "/home/vla/.pysnmp/mibs" ],
		[ "SNMPv2-MIB", "IF-MIB", "SNMP-COMMUNITY-MIB", "XPPC-MIB", "POLYGON-MIB", "POLYCOM740-MIB" ]
	)
	test("127.0.0.18", 54321, 10, "trap", "area", test.callback)







