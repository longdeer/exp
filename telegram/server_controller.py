import	os
from	typing								import Tuple
from	time								import sleep
from	telebot								import TeleBot
from	telebot.types						import Message
from	pygwarts.magical.time_turner		import TimeTurner
from	pygwarts.magical.time_turner.timers	import mostsec
from	pygwarts.magical.spells				import patronus
from	pygwarts.irma.contrib				import LibraryContrib
from	credistr							import tlg_id_lngd
from	credistr							import tlg_bot_serverbot
from	lngd_local_scanner					import byte_scan
from	navbow								import NavbowController








def server_controller(
						BOT		:TeleBot,
						Navbow	:NavbowController,
						logger	:LibraryContrib,
						tpoint	:TimeTurner,
						user	:int,
						command	:str,
						args	:Tuple[str,]
					):

	"""
		Implements following operations:
		help		- show this message
		uptime		- show uptime of the BOT
		lsnavtex	- list NAVTEX fiels
		cat			- view navtex NAME file
		zinspect	- show Navbow zero state words
		sinspect	- show Navbow states for words from arguments
		zconvert	- convert Navbow zero state words to one state (all or from arguments)
		oconvert	- convert Navbow one state words to zero state (only from arguments)
		zerase		- erase Navbow zero state words (all or from arguments)
		add			- add Navbow words with state
		kill		- stop bot
	"""

	match command:

		case "kill":

			logger.handover("handler", assign=False)
			logger.info("Commence controller killing")
			BOT.send_message(user, "bye")

			raise StopIteration


		case "uptime":

			uptime = mostsec(TimeTurner().diff(subtrahend=tpoint))
			response = f"uptime {uptime}"
			logger.handover("handler", assign=False)
			logger.info(f"Reporting uptime {uptime}")


		case "help":

			response = server_controller.__doc__
			logger.handover("handler", assign=False)
			logger.info("Help message formed")


		case "lsnavtex":

			response = "\n".join(os.listdir("/srv/A2/R/CKS/ARQ/NAVTEX/"))
			logger.handover("handler", assign=False)
			logger.info("Navtex directory listing: " + response.replace("\n",", "))


		case "cat":

			if	(response := "\n".join(
			
				byte_scan(os.path.join("/srv/A2/R/CKS/ARQ/NAVTEX/", F.upper()))[1]
				for F in args

			))	and not response.isspace():

				logger.handover("handler", assign=False)
				logger.info(f"Navtex files listing: {len(response)} symbols")


		case "zinspect":

			Navbow.NavbowShelve.grab("/srv/lcontainer/hagrid/Navbag.Shelf", rewrite=True)
			inspection = Navbow.inspect_state(0)["unknown"]

			if		inspection: response = "unknown words: " + ", ".join(inspection)
			else:	response = "no unknown words found"


		case "sinspect":

			Navbow.NavbowShelve.grab("/srv/lcontainer/hagrid/Navbag.Shelf", rewrite=True)
			inspection = Navbow.inspect(*args)
			response = str()

			if	inspection["known"]: response += "known words: " + ", ".join(inspection["known"]) + "\n"
			if	inspection["unknown"]: response += "unknown words: " + ", ".join(inspection["unknown"]) + "\n"
			if	inspection["undefined"]: response += "undefined words: " + ", ".join(inspection["undefined"])


		case "zconvert":

			Navbow.NavbowShelve.grab("/srv/lcontainer/hagrid/Navbag.Shelf", rewrite=True)
			words = args or Navbow.inspect_state(0)["unknown"]
			converted = Navbow.convert(*words, state=1)["converted"]
			Navbow.NavbowShelve.produce("/srv/lcontainer/hagrid/Navbag.Shelf", magical=True)

			if		converted: response = "words converted: " + ", ".join(converted)
			else:	response = "no words converted to known"


		case "oconvert":

			if	args:

				Navbow.NavbowShelve.grab("/srv/lcontainer/hagrid/Navbag.Shelf", rewrite=True)
				converted = Navbow.convert(*args, state=0)["converted"]
				Navbow.NavbowShelve.produce("/srv/lcontainer/hagrid/Navbag.Shelf", magical=True)

				if		converted: response = "words converted: " + ", ".join(converted)
				else:	response = "no words converted to unknown"
			else:		response = "can convert only specified words to unknown"


		case "add":

			if	args:

				Navbow.NavbowShelve.grab("/srv/lcontainer/hagrid/Navbag.Shelf", rewrite=True)
				added = Navbow.add(*args[:-1], state=args[-1])
				Navbow.NavbowShelve.produce("/srv/lcontainer/hagrid/Navbag.Shelf", magical=True)

				if(added["added to known"]): response = "added known: " + ", ".join(added["added to known"])
				elif(added["added to unknown"]): response = "added unknown: " + ", ".join(added["added to unknown"])
				else: response = "no words added"


		case "zerase":

			Navbow.NavbowShelve.grab("/srv/lcontainer/hagrid/Navbag.Shelf", rewrite=True)
			erased = Navbow.erase_state(0)["unknown erased"]
			Navbow.NavbowShelve.produce("/srv/lcontainer/hagrid/Navbag.Shelf", rewrite=True)

			if		erased: response  = "unknown words erased: " + ", ".join(erased)
			else:	response = "no unknown words erased"


		case _:

			logger.handover("handler", assign=False)
			logger.info("Command not recognized")
			response = f"command \"{command}\" not recognized"


	if	response and not response.isspace() and (timeout := 1):
		for i in range(0, len(response), 4096):

			BOT.send_message(user, response[i:i+4096])

			sleep(timeout)
			timeout += 1
	else:

		logger.handover("handler", assign=False)
		logger.warning("Response was not formed")
		BOT.send_message(user, "response was not formed")








if	__name__ == "__main__":


	T		= TimeTurner()
	BOT		= TeleBot(tlg_bot_serverbot())
	ALLOWED	= [ int(tlg_id_lngd()) ]
	LOGGY	= LibraryContrib(

		handler="/srv/lcontainer/sndbx/v-server-controller/server_controller.loggy",
		init_name="server-controller-bot",
	)
	NAVBOW	= NavbowController(LOGGY, reclaiming=True)


	@BOT.message_handler(content_types=[ "text" ])
	def controller(request :Message):

		user = request.chat.id
		message = request.text
		command, *args = message.split(" ")

		LOGGY.handover("handler", assign=False)
		LOGGY.info(f"Processing user id {user} message \"{message}\"")

		if	user not in ALLOWED:

			BOT.send_message(user, "sorry, your id not allowed")
			LOGGY.handover("handler", assign=False)
			LOGGY.info(f"User id {user} declined")

			raise StopIteration

		try:	server_controller(BOT, NAVBOW, LOGGY, T, user, command, args)
		except	StopIteration : raise
		except	Exception as E:

			response = patronus(E)
			BOT.send_message(user, response)
			LOGGY.handover("handler", assign=False)
			LOGGY.warning(f"Processing failed with {response}")


	LOGGY.handover("handler", assign=False)
	LOGGY.info("Starting server controller bot")


	try:	BOT.polling(non_stop=True, interval=0)
	except	StopIteration:

		LOGGY.handover("handler", assign=False)
		LOGGY.info("Stopped by kill command")
		BOT.stop_bot()







