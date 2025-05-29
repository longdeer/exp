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
import	mysql.connector








def server_controller(
						BOT		:TeleBot,
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


			db = mysql.connector.connect(

				user="hoperator",
				password="hoperator::SQL",
				host="127.0.0.1",
				database="tserverdb",
			)
			table = db.cursor()
			table.execute("SELECT word FROM navbag WHERE state = 0")
			answer = ", ".join( row[0] for row in table )

			if		answer: response = "unknown words: " + answer.rstrip(", ")
			else:	response = "no unknown words found"

			table.close()
			db.close()


		case "sinspect":


			if	(words := set(map(str.upper,args))):

				db = mysql.connector.connect(

					user="hoperator",
					password="hoperator::SQL",
					host="127.0.0.1",
					database="tserverdb",
				)
				table = db.cursor()
				table.execute(

					"SELECT word,state FROM navbag WHERE word IN (%s)"%(
						",".join(map(lambda W : f"'{W}'", words))
					)
				)
				answer = dict(table)
				known = list()
				unknown = list()
				undefined = list()
				response = str()

				for word in words:
					match answer.get(word):

						case None:	undefined.append(word)
						case 0:		unknown.append(word)
						case 1:		known.append(word)

				table.close()
				db.close()

				if	known: response += "known words: " + ", ".join(known) + "\n"
				if	unknown: response += "unknown words: " + ", ".join(unknown) + "\n"
				if	undefined: response += "undefined words: " + ", ".join(undefined)
			else:	response = "no words to inspect provided"


		case "zconvert":


			db = mysql.connector.connect(

				user="hoperator",
				password="hoperator::SQL",
				host="127.0.0.1",
				database="tserverdb",
			)
			table = db.cursor()

			if	(words := set(args)):

				table.execute(

					"UPDATE navbag SET state = 1 WHERE word IN (%s)"%(
						",".join(map(lambda W : f"'{W}'", words))
					)
				)
			else:	table.execute("UPDATE navbag SET state = 1 WHERE state = 0")

			response = "done update to known"

			db.commit()
			table.close()
			db.close()


		case "oconvert":


			if	(words := set(args)):

				db = mysql.connector.connect(

					user="hoperator",
					password="hoperator::SQL",
					host="127.0.0.1",
					database="tserverdb",
				)
				table = db.cursor()
				table.execute(

					"UPDATE navbag SET state = 0 WHERE word IN (%s)"%(
						",".join(map(lambda W : f"'{W}'", words))
					)
				)

				response = "done update to unknown"

				db.commit()
				table.close()
				db.close()

			else:	response = "words to convert not provided"


		case "add":


			match args:

				case ( "0" | "1" as state, *rest ):
					if	(words := set(map(str.upper,rest))):

						db = mysql.connector.connect(

							user="hoperator",
							password="hoperator::SQL",
							host="127.0.0.1",
							database="tserverdb",
						)
						table = db.cursor()
						upd = str()
						query = str()

						for word in words:

							query += f"('{word}',{state}),"
							upd += f"{word}, "

						table.execute("INSERT IGNORE INTO navbag (word,state) VALUES %s"%query.rstrip(","))
						response = "words added to %s: %s"%(
							"known" if int(state) else "unknown", upd.rstrip(", ")
						)
						db.commit()
						table.close()
						db.close()

					else:	response = "no words to add provided"
				case _:		response = "incorrect state"


		case "zerase":


			db = mysql.connector.connect(

				user="hoperator",
				password="hoperator::SQL",
				host="127.0.0.1",
				database="tserverdb",
			)
			table = db.cursor()

			if	(words := set(args)):

				table.execute(

					"DELETE FROM navbag WHERE word IN (%s)"%(
						",".join(map(lambda W : f"'{W}'", words))
					)
				)
			else:	table.execute("DELETE FROM navbag WHERE state = 0")

			response = "done erasing unknown"

			db.commit()
			table.close()
			db.close()


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

		handler="/srv/lcontainer/sndbx/v-server-mysql-controller/server_controller.loggy",
		init_name="server-mysql-controller-bot",
	)


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

		try:	server_controller(BOT, LOGGY, T, user, command, args)
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







