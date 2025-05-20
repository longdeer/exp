from typing									import List
from os										import listdir
from time									import sleep
# from sys									import exit
from telebot								import TeleBot
from telebot.types							import Message
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.time_turner			import TimeTurner
from pygwarts.magical.spells				import patronus
# from pygwarts.magical.time_turner.timers	import Sectimer
from pygwarts.irma.shelve					import LibraryShelf
from pygwarts.irma.contrib					import LibraryContrib
# from pygwarts.hagrid.cultivation.navtex		import NavBoW2
from credistr								import tlg_id_lngd
from credistr								import tlg_bot_serverbot

















def server_controller(BOT :TeleBot, user :int, message :str, logger :LibraryContrib):

	"""
		Implements following operations:
		help		- show this message
		uptime		- show uptime of the BOT
		loggy		- parse DATE MODULE NAME [LEVEL] loggy variations like:
		04/06/2023,1442 hagrid navdrop [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 hagrid softsync [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 hagrid hardsync [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 hagrid arch [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 hagrid,navBoW navBoW [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 filch discovery [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 filch broadwatch [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 filch polywatch [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 hedwig report [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 irma library [INFO/WARNING/ERROR/CRITICAL]
		04/06/2023,1442 irma,annex library INFO/WARNING/ERROR/CRITICAL
		lsplot		- list DATE plots
		plot		- send broadwatch plot, sinopsis DATE NAME, like 05/06/2023 total
		lsnavtex	- list NAVTEX fiels
		cat			- view navtex NAME file
		catcron		- list NAME cronloggy, like hagrid,filch,irma,hedwig,tlgbot
		zinspect	- show all zero values words
		winspect	- show words from arguments
		zconvert	- convert one values to zero values wrods
		oconvert	- convert zero values to one values words
		zerase		- erase all or provided zero values words
		kill		- stop bot by exiting the process
	"""


	try:


		command, *args = message.split(" ")


		match command:


			case "help":

				response = server_controller.__doc__
				logger.info("Help message formed")

			case "kill":

				logger.info("Commence killing command")
				BOT.send_message(user, "bye")
				raise StopIteration

			case _:

				logger.info("Command not recognized")
				response = f"command \"{command}\" not recognized"

		# if command == "help": response = ServerController.__doc__
		## elif command == "uptime": response = Sectimer.sectimer(TimeTurner().diff(subtrahend=start_timer)[2])


	# 	elif command == "loggy":
	# 		try:
	# 			try: date, module, name, level = args[:4]
	# 			except ValueError:

	# 				date, module, name = args[:3]
	# 				level = None


	# 			try:	D,T = date.split(",")
	# 			except: D,T = date,None


	# 			try:
	# 				module, submodule = module.split(",")
	# 				response = f"{module} {submodule} {name} {level}s loggy for {date}:\n"
	# 				module = f"{module}/{submodule}"
	# 				sub = True


	# 			except ValueError:

	# 				response = f"{module} {name} {level}s loggy for {date}:\n"
	# 				module = f"{module}/{name}"
	# 				sub = False


	# 			_date = TimeTurner(D)
	# 			date_line = f"{D} {T}" if T else D
	# 			_level = level if not level else level.upper()


	# 			if sub and submodule == "navBoW":
	# 				try:
	# 					with open(f"/srv/lcontainer/{module}/g{submodule}.loggy") as LOGGY:
	# 						for line in LOGGY:
	# 							if date_line in line:
	# 								if _level is not None:
	# 									if _level in line:

	# 										response += line
	# 								else:	response += line


	# 				except Exception as E:
	# 					response += f"exception caught: \"{E}\""


	# 			elif sub and submodule == "annex":
	# 				try:
	# 					with open(f"/srv/lcontainer/{module}/{_date.Ym_aspath}/g{name}{_date.dmY_asjoin}.{submodule}") as ANNEX:
	# 						for line in ANNEX:

	# 							response += line


	# 				except Exception as E:
	# 					response += f"exception caught: \"{E}\""


	# 			else:
	# 				try:
	# 					with open(f"/srv/lcontainer/{module}/{_date.Ym_aspath}/g{name}{_date.dmY_asjoin}.loggy") as LOGGY:
	# 						for line in LOGGY:
	# 							if date_line in line:
	# 								if _level is not None:
	# 									if _level in line:

	# 										response += line
	# 								else:	response += line


	# 				except Exception as E:
	# 					response += f"exception caught: \"{E}\""


	# 		except Exception as E:
	# 			response = f"couldn't hanlde \"loggy\" command due to: \"{E}\""




	# 	elif command == "catcron":

	# 		name = args[0]
	# 		response = str()


	# 		if name == "tlgbot":	cronpath = "/srv/lcontainer/gsandbox/v-tlgbot/tlgbot.cronloggy"
	# 		else:					cronpath = f"/srv/lcontainer/{name}/{name}.cronloggy"


	# 		try:
	# 			response = f"cronloggy for {name}:\n"
	# 			with open(cronpath) as CRONLOGGY:
	# 				for line in CRONLOGGY:

	# 					response += f"{line}\n"


	# 		except Exception as E:
	# 			response = f"couldn't view {name} cronloggy due to: \"{E}\""




	# 	elif command == "lsplot":

	# 		response = str()
	# 		try:
	# 			for item in listdir(f"/srv/dump/bwvisual/{TimeTurner(args[0]).Ymd_aspath}"):
	# 				response += f"{item}\n"


	# 		except Exception as E:
	# 			response = f"couldn't list plots due to: \"{E}\""




	# 	elif command == "plot":
	# 		try:
	# 			date, name = args[:2]
	# 			D = TimeTurner(date)


	# 			with open(f"/srv/dump/bwvisual/{D.Ymd_aspath}/{name}_{D.dmY_asjoin}.png", "rb") as PLOT:

	# 				self.BOT.send_document(message.chat.id, PLOT)
	# 				response = f"{name}_{D.dmY_asjoin} plot"


	# 		except Exception as E:
	# 			response = f"couldn't hanlde plot due to: \"{E}\""




	# 	elif command == "lsnavtex":

	# 		response = str()
	# 		for item in listdir("/srv/A2/R/CKS/ARQ/NAVTEX/"):
	# 			if item.upper().endswith(".TLX"): response += f"{item}\n"




	# 	elif command == "cat":
	# 		try:
	# 			file = args[0]
	# 			response = f"{file}\n"


	# 			with open(f"/srv/A2/R/CKS/ARQ/NAVTEX/{file}") as MESSAGE:
	# 				for line in MESSAGE:
	# 					response += f"{line}\n"


	# 		except Exception as E:
	# 			response = f"couldn't view \"{args}\" due to: \"{E}\""




	# 	elif command == "zinspect":

	# 		navbow = CurrentBoW()
	# 		response = navbow.zinspect()


	# 		if response:	response = "current zeros:\n" + response
	# 		else: 			response = "no current zeros"


	# 		del navbow




	# 	elif command == "winspect":

	# 		navbow = CurrentBoW()
	# 		response = navbow.winspect(*args)


	# 		if not response: response = "no response for winspect"
	# 		del navbow




	# 	elif command == "zconvert":

	# 		navbow = CurrentBoW()
	# 		response = navbow.zconvert(*args)


	# 		if response:	response = "zero converting result:\n" + response
	# 		else:			response = "no result for zero converting"


	# 		del navbow




	# 	elif command == "oconvert":

	# 		navbow = CurrentBoW()
	# 		response = navbow.oconvert(*args)


	# 		if response:	response = "one converting result:\n" + response
	# 		else:			response = "no result for one converting"


	# 		del navbow




	# 	elif command == "zerase":

	# 		navbow = CurrentBoW()
	# 		response = navbow.zerase(*args)


	# 		if response:	response = "zero erasing result:\n" + response
	# 		else:			response = "no result for zero erasing"


	# 		del navbow




	# 	elif command == "kill":

	# 		self.BOT.send_message(message.chat.id, "commence killing command")
	# 		raise StopIteration


	# 	else: response = f"command \"{command}\" not recognized"


	except StopIteration: raise
	except Exception as E: response = patronus(E)


	timeout = 0
	for i in range(0, len(response), 4096):

		BOT.send_message(user, response[i:i+4096])

		timeout += 1
		sleep(timeout)








if	__name__ == "__main__":


	ALLOWED	= [ int(tlg_id_lngd()) ]
	LOGGY	= LibraryContrib(init_name="server", handler=f"server_controller.loggy")
	BOT		= TeleBot(tlg_bot_serverbot())


	@BOT.message_handler(content_types=[ "text" ])
	def controller(request :Message):

		user = request.chat.id
		message = request.text

		LOGGY.info(f"Processing user id {user} request")
		LOGGY.info(f"Recieved message \"{message}\"")

		if	user not in ALLOWED:

			BOT.send_message(user, "sorry, your id not allowed")
			LOGGY.info(f"User id {user} declined")
			raise StopIteration
		else:
			server_controller(BOT, user, message, LOGGY)


	try:	BOT.polling(non_stop=True, interval=0)
	except	StopIteration:

		LOGGY.info("Stopped by kill command")
		BOT.stop_bot()







